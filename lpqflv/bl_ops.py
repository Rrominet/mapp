import bpy 
from lpqflv import log
from lpqflv import bl_utils
from lpqflv import bl_font

def registerAll(toRegister) : 
    if type(toRegister) is dict : 
        for cl in toRegister["ops"] : 
            bpy.utils.register_class(cl)
    else : 
        for cl in toRegister.ops : 
            bpy.utils.register_class(cl)


def unregisterAll(toRegister) : 
    for cl in reversed(toRegister) : 
        bpy.utils.unregister_class(cl)

def clean(cfg) : 
    if type(cfg) is dict : 
        unregisterAll(cfg["ops"])
        cfg["ops"] = []
    else : 
        unregisterAll(cfg.ops)
        cfg.ops = []


class Operator (bpy.types.Operator) : 
    bl_label=""
    bl_options = {
               'REGISTER',
               'UNDO' 
            }

    bl_description = ""
    trough = False
    font = None
    width = 350

    # you can change that if you don't want the OK button at the end of the dialog
    okButton = True

    #You can put this as False if you want the draw function to be used for the Undo/Redo Window instead of a dialog before executing the operator
    drawAsDialog = True

    def createProgress(self, total) : 
        self.font = bl_font.Font("Progress : 0/" + str(total))
        self.font.draw()
        bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

    def setProgress(self, doned, total) : 
        self.font.setText("Progress : " + str(doned) + "/" + str(total))
        bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

    def redraw(self) : 
        bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

    def clearProgress(self):
        self.font.clear()

    def overInvoke(self, ctx, e) : 
        pass

    def invokeDraw(self, ctx) : 
        wm = ctx.window_manager
        if self.okButton : 
            return wm.invoke_props_dialog(self, width=self.width)
        else :
            return wm.invoke_popup(self, width=self.width)

    def invoke(self, ctx, e) : 
        self.overInvoke(ctx, e) 
        if self.hasDraw() : 
            return self.invokeDraw(ctx)
        elif self.hasModal() : 
            ctx.window_manager.modal_handler_add(self)
            if self.trough : 
                return {'PASS_THROUGH'}
            else : 
                return {'RUNNING_MODAL'}
        else : 
            return self.execute(ctx)

    def execute(self, ctx) : 
        return {"FINISHED"}

    def hasDraw(self) : 
        if hasattr(self, "draw") and self.drawAsDialog : 
            return True 
        else : 
            return False

    def hasModal(self) : 
        if hasattr(self, "modal") : 
            return True 
        else : 
            return False

    @classmethod
    def init(cls, toRegister) : 
        if type(toRegister) is dict : 
            toRegister["ops"].append(cls)
        else : 
            toRegister.ops.append(cls)

#will return the options of a blender property setted as an anotation in OperatorCls
#the returned object is a dict
def propOptions(OperatorCls, propname) :
    return OperatorCls.__annotations__[propname].keywords

class Property : 
    def __init__(self, propname, key, _type, step = 1, cleanName="", items=None) : 
        self.prop = propname
        self.key = key
        self.type = _type
        self.step = step
        if cleanName == "" : 
            self.name = propname
        else : 
            self.name = cleanName

        self.items = None
        if items : 
            self.items = []
            for i in items : 
                self.items.append(i[0])
        self.itemsIdex = 0

operators_properties = {}

#you need to override overModal here.
#the main action need to be executed in the execute method (you could write cal it in overModal if you want.)
# the big thing in the class is the the class method makePropModifiable. See its doc.
class ModalOperator (Operator) : 
    MOUSE_SIDE = 0
    MOUSE_UP = 1
    WHEEL = 2
    SLOW = 3
    FAST = 4
    NORMAL = 5
    SWITCH = 6 # used for bool variable automaticly

    header_txt = ""
    propmouseup = None
    propmouseside = None
    propwheel = None

    speed = NORMAL

    #We don't want the dialog overriding the modal operator
    drawAsDialog = False

    #you need to override this in you child class
    def overModal(self, ctx, e) :
        pass

    #will make a property managable by mouse mouvement in the modal mode of the operator.
    #the key is the key to press to activate the property management.
    #If empty, it is managed by default - you can refocus on it in the modal operator after focused on another option with 'TAB'.
    #the type represent the way the prop will be managed : by mouse (up/side) or by wheel.
    #
    #The property given can be a int, float or an Enum. (could support bool later...)
    @classmethod
    def makePropModifiable(cls, propname, key="", _type=MOUSE_SIDE, step = 1) : 
        if cls.bl_idname not in operators_properties :
            operators_properties[cls.bl_idname] = []

        opt = propOptions(cls, propname)
        if "items" in opt :
            operators_properties[cls.bl_idname].append(Property(propname, key.upper(), _type, step, opt["name"], opt["items"]))
        else :
            operators_properties[cls.bl_idname].append(Property(propname, key.upper(), _type, step, opt["name"]))

    def drawProp(self, prop) :
        if self.header_txt != "" : 
            self.header_txt += " | "
        try : 
            self.header_txt += prop.name + " : " + str(round(getattr(self, prop.prop), 3))
        except :
            self.header_txt += prop.name + " : " + str(getattr(self, prop.prop)).lower().capitalize()
        self.header_txt += " ("
        if prop.type == ModalOperator.MOUSE_SIDE :
            self.header_txt += "Side"
        elif prop.type == ModalOperator.MOUSE_UP :
            self.header_txt += "Up"
        elif prop.type == ModalOperator.WHEEL :
            self.header_txt += "Wheel"
        if prop.key != "" : 
            self.header_txt += " - " + prop.key 
        self.header_txt += ")"

    def drawProps(self, ctx) :
        self.header_txt = ""
        if self.__class__.bl_idname in operators_properties :
            for prop in operators_properties[self.__class__.bl_idname] : 
                self.drawProp(prop)
        if self.speed == ModalOperator.SLOW :
            self.header_txt += " | - SLOW"
        elif self.speed == ModalOperator.FAST :
            self.header_txt += " | - FAST"
        ctx.area.header_text_set(self.header_txt)

    def manageEvents(self, ctx, e) : 
        if self.__class__.bl_idname in operators_properties :
            for p in operators_properties[self.__class__.bl_idname] : 
                if e.value == "PRESS" : 
                    if p.key == e.type or (p.key == "" and e.type == "TAB") : 
                        if p.type == ModalOperator.MOUSE_SIDE : 
                            self.propmouseside = p
                        elif p.type == ModalOperator.MOUSE_UP : 
                            self.propmouseup = p
                        elif p.type == ModalOperator.WHEEL : 
                            self.propwheel = p
                        elif p.type == ModalOperator.SWITCH : 
                            setattr(self, p.prop, not getattr(self, p.prop))

        if e.type == "WHEELUPMOUSE" : 
            if self.propwheel : 
                self.addToPropValue(self.propwheel)

        elif e.type == "WHEELDOWNMOUSE" : 
            if self.propwheel : 
                self.addToPropValue(self.propwheel, -1)

        elif e.type == "MOUSEMOVE" : 
            if self.propmouseside : 
                delta = e.mouse_x - e.mouse_prev_x
                self.addToPropValue(self.propmouseside, delta)

            if self.propmouseup : 
                delta = e.mouse_y - e.mouse_prev_x
                self.addToPropValue(self.propmouseup, delta)

    def addToPropValue(self, prop, delta=1) :
        delta = float(delta)
        if self.speed == ModalOperator.SLOW :
            delta /= 10
        elif self.speed == ModalOperator.FAST :
            delta *= 10

        if prop.items : 
            prop.itemsIdex +=1
            if prop.itemsIdex >= len(prop.items) : 
                prop.itemsIdex = 0
            setattr(self, prop.prop, prop.items[prop.itemsIdex])
        else :
            try : 
                setattr(self, prop.prop, getattr(self, prop.prop) + delta * prop.step)
            except :
                setattr(self, prop.prop, getattr(self, prop.prop) + int(delta) * prop.step)

    def invoke(self, ctx, e) :
        res = super().invoke(ctx, e)
        self.header_txt = ""
        self.propmouseup = None
        self.propmouseside = None
        self.propwheel = None
        self.speed = ModalOperator.NORMAL
        if self.__class__.bl_idname in operators_properties :
            for p in operators_properties[self.__class__.bl_idname] : 
                if p.key == "" : 
                    if p.type == ModalOperator.MOUSE_SIDE : 
                        self.propmouseside = p
                    elif p.type == ModalOperator.MOUSE_UP : 
                        self.propmouseup = p
                    elif p.type == ModalOperator.WHEEL : 
                        self.propwheel = p
        return res

    #this is called just after the last call of self.execute
    #typically when the user user press enter or left click to valid his action.
    #you need to override it if you want to execute some code at this moment.
    def onFinished(self, ctx) :
        pass

    def placeCursor(self, ctx, e) :
        if e.mouse_region_x < ctx.area.x : 
            ctx.window.cursor_warp(ctx.area.x + ctx.area.width, e.mouse_y)
        elif e.mouse_region_x > ctx.area.x + ctx.area.width :
            ctx.window.cursor_warp(ctx.area.x, e.mouse_y)

        if e.mouse_region_y <= ctx.area.y : 
            ctx.window.cursor_warp(e.mouse_x, ctx.area.y + ctx.area.height)
        elif e.mouse_region_y >= ctx.area.y + ctx.area.height :
            ctx.window.cursor_warp(e.mouse_x, ctx.area.y)

    def modal(self, ctx, e) : 
        self.placeCursor(ctx, e)
        if e.type == "ESC" or e.type=="RIGHTMOUSE" : 
            ctx.area.header_text_set(None)
            self.cancel(ctx)
            return {"CANCELLED"}
        elif (e.type == "RET" and e.value == "PRESS") or e.type == "LEFTMOUSE": 
            ctx.area.header_text_set(None)
            r = self.execute(ctx)
            self.onFinished(ctx)
            return r

        if e.shift : 
            self.speed = ModalOperator.SLOW
        elif e.alt : 
            self.speed = ModalOperator.FAST
        else : 
            self.speed = ModalOperator.NORMAL

        self.drawProps(ctx)
        self.manageEvents(ctx, e)
        self.overModal(ctx, e)
        ctx.area.tag_redraw()

        return {"RUNNING_MODAL"}

class KeyEventInfos :
    def __init__(self, key="", ctrl=False, alt=False, shift=False, oskey=False) :
        self.key = key
        self.ctrl = ctrl
        self.alt = alt
        self.shift = shift
        self.oskey = oskey

    def checkNumbers(self, v) : 
        match v : 
            case "zero" : 
                return "0"
            case "one" : 
                return "1"
            case "two" : 
                return "2"
            case "three" : 
                return "3"
            case "four" : 
                return "4"
            case "five" : 
                return "5"
            case "six" : 
                return "6"
            case "seven" : 
                return "7"
            case "eight" : 
                return "8"
            case "nine" : 
                return "9"

            case "numpad_0" : 
                return "0"
            case "numpad_1" : 
                return "1"
            case "numpad_2" : 
                return "2"
            case "numpad_3" : 
                return "3"
            case "numpad_4" : 
                return "4"
            case "numpad_5" : 
                return "5"
            case "numpad_6" : 
                return "6"
            case "numpad_7" : 
                return "7"
            case "numpad_8" : 
                return "8"
            case "numpad_9" : 
                return "9"

            case "semi_colon" :
                return ";"
            case "period" : 
                return "."
            case "comma" : 
                return ","
            case "quote" : 
                return "“"
            case "accent_grave" : 
                return "`"
            case "minus" : 
                return "-"
            case "plus" : 
                return "+"
            case "slash" : 
                return "/"
            case "back_slash" : 
                return "\\"
            case "equal" : 
                return "="
            case "left_bracket" : 
                return "["
            case "right_bracket" : 
                return "]"
        return v

    def value(self) : 
        v = self.key
        v = self.checkNumbers(v)
        if self.shift : 
            v = v.upper()
        if self.oskey : 
            v = "o-" + v
        if self.alt : 
            v = "a-" + v
        if self.ctrl : 
            v = "c-" + v
        return v

class ComplexKeybindOperator(bpy.types.Operator) : 
    filters = ("mouse", "pen", "eraser", "timer", "window", "motion", "button", "zone", "alt", "ctrl", "os", "shift")
    #take an object of type KeyEventInfos as arg
    onKeyEvents = []

    # if one of these functions return True, the modal operator finish
    condsToQuit = []

    def modal(self, ctx, event) : 
        if event.type == "ESC" : 
            return {'FINISHED'}
        if event.value != "PRESS" : 
            return {'RUNNING_MODAL'}
        ctx.area.tag_redraw()
        t = event.type.lower()
        for n in self.filters : 
            if n in t : 
                return {'RUNNING_MODAL'}

        for f in self.onKeyEvents : 
            f(KeyEventInfos(t, event.ctrl, 
                            event.alt, 
                            event.shift, 
                            event.oskey))

        for c in self.condsToQuit : 
            if c() : 
                return {'FINISHED'}
        return {'RUNNING_MODAL'}

    def invoke(self, ctx, event) : 
        ctx.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


_toUnRegister = []
def create(idname, execute=None, invoke=None, label="", description="") : 
    class op (bpy.types.Operator) : 
        bl_idname = idname
        bl_label = label
        bl_description = description
        bl_options = {'REGISTER', 'UNDO'}

        def execute(self, ctx) : 
            if execute is not None :
                return execute(self, ctx)
            return {'FINISHED'}

        def invoke(self, ctx, e) :
            if invoke is not None :
                return invoke(self, ctx, e)
            return self.execute(ctx)

    bpy.utils.register_class(op)
    _toUnRegister.append(op)

def unregister() : 
    for op in _toUnRegister : 
        bpy.utils.unregister_class(op)
