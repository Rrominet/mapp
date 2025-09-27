#this is a file that add some usefule function to the blender ui system.
#It will often expend the UILayout functionalities. It's why the functions in this file will often take a UILayout object as a first argument.

from lpqflv import bl_utils
import bpy

# TODO
# will use some bool properties to draw a tabs in the ui
# when settin a bool property to True it will set the others to False.
#you still need to manage the tab drawing after ward checking the prop value.
def tabs(layout, *boolProps) : 
    pass

#return a items tuple list for the prop Enum
def items(*args) : 
    _r = []
    for i in range(len(args)) : 
        _r.append((args[i].replace(" ", ""), args[i], "", i))
    return _r

def menus() : return bl_utils.menus()
def panels() : return bl_utils.panels()
def headers() : return bl_utils.headers()

#this will be the dir that contains all menus operators infos
#The key will be the Menu.bl_idname
menu_ops = {}

class Menu (bpy.types.Menu) :
    #params could be the the params props of the Operatar key : value of the operator context as context : "INVOKE_DEFAULT" for example 
    @staticmethod
    def addOp(bl_idname, OperatorCls, params={}) : 
        if not bl_idname in menu_ops : 
            menu_ops[bl_idname] = []
        menu_ops[bl_idname].append({"operator" : OperatorCls, "params" : params})

    def draw(self, context) : 
        self.overDraw(context)
        for o in menu_ops[self.bl_idname]["operator"] : 
            params = o["params"]
            if "context" in params : 
                self.layout.operator_context = params["context"]
            if "icon" in params : 
                self.layout.operator(o["operator"].bl_idname, icon=params["icon"])
            else :
                self.layout.operator(o["operator"].bl_idname)

    #you need to override this if you want to draw something before the operators
    def overDraw(self, context) : 
        pass
    #this return a class (not an instance)
    @staticmethod
    def create(category="OBJECT", draw=None, operators=[]) : 
        pass

