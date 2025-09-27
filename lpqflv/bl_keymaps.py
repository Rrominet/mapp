import bpy 
from lpqflv import errors as error
from lpqflv import bl_ops

def unregister(keyMapsList) : 
    for km, kmi in keyMapsList : 
        km.keymap_items.remove(kmi)
    keyMapsList.clear()

spaces = ["EMPTY", 
        "VIEW_3D", 
        "IMAGE_EDITOR", 
        "NODE_EDITOR", 
        "SEQUENCE_EDITOR", 
        "CLIP_EDITOR", 
        "DOPESHEET_EDITOR", 
        "GRAPH_EDITOR",
        "NLA_EDITOR", 
        "TEXT_EDITOR", 
        "CONSOLE", 
        "INFO", 
        "OUTLINER", 
        "PROPERTIES", 
        "FILE_BROWSER", 
        "SPREADSHEET", 
        "PREFERENCES", 
        ]

categories = {
        "EMPTY" : "Window",
        "VIEW_3D" : "3D View Generic",
        "IMAGE_EDITOR" : "Image", 
        "NODE_EDITOR" : "Node Editor", 
        "SEQUENCE_EDITOR" : "Sequencer", 
        "CLIP_EDITOR" : "Clip", 
        "DOPESHEET_EDITOR" : "Dopesheet", 
        "GRAPH_EDITOR" : "Graph Editor",
        "NLA_EDITOR" : "NLA Editor", 
        "TEXT_EDITOR" : "Text", 
        "CONSOLE" : "Console", 
        "INFO" : "Info", 
        "OUTLINER" : "Outliner", 
        "PROPERTIES" : "Property Editor", 
        "FILE_BROWSER" : "File Browser", 
        "SPREADSHEET" : "Spreadsheet", 
        "PREFERENCES" : "User Interface", 
        }

items = []
i = 0
for c in categories : 
    items.append((c, categories[c], "", i))
    i+=1

def newKeyMaps(op_idname, 
        keyMapsList, 
        touch, 
        spaceTypes = spaces, 
        menu=False, 
        pshift=False, 
        palt=False, 
        pctrl=False, 
        ptype="PRESS",
        ClsPrefs=None) : 
    for i in range(len(spaceTypes)) : 
        newKeyMap(op_idname, keyMapsList, touch, categories[spaceTypes[i]], spaceTypes[i], menu, pshift, palt, pctrl, ptype, ClsPrefs)

def newKeyMap(op_idname, 
        keyMapsList, 
        touch, 
        category = None, 
        spaceType = "VIEW_3D", 
        menu=False, 
        pshift=False, 
        palt=False, 
        pctrl=False, 
        ptype="PRESS",
        ClsPrefs=None) : 
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if not category : 
        category = categories[spaceType]
    if category not in kc.keymaps : 
        km = kc.keymaps.new(name=category, space_type=spaceType)
    else : 
        km = kc.keymaps[category]

    if menu  : 
        kmi = km.keymap_items.new("wm.call_menu", 
                value = ptype,
                type=touch,
                shift = pshift, 
                alt=palt, 
                ctrl = pctrl)
        kmi.properties.name = op_idname
    else :
        kmi = km.keymap_items.new(op_idname, 
                value = ptype,
                type=touch,
                shift = pshift, 
                alt=palt, 
                ctrl = pctrl)
    keyMapsList.append((km, kmi))
    if ClsPrefs : 
        ClsPrefs.keyMapsList = keyMapsList

class KeyMapsPrefs(bpy.types.AddonPreferences) : 
    keyMapsList = []
    def overDraw(self, ctx) : 
        pass

    def draw(self, ctx) : 
        self.overDraw(ctx)
        self.drawKeymaps(ctx)

    def drawKeymaps(self, ctx) : 
        if len(self.keyMapsList) == 0 : 
            return
        box = self.layout.box()
        r = box.row()
        r.label(text="Shortcuts : ", icon="EVENT_RETURN")

        for km, kmi in self.keyMapsList : 
            self.drawForKeyMapItem(box, kmi)

    def drawForKeyMapItem(self, layout, kmi) :
        r = layout.row(align=True)
        r.label(text=kmi.name)
        r.prop(kmi, "map_type")
        r.prop(kmi, "type", text="Key")
        r.prop(kmi, "shift_ui", icon="EVENT_SHIFT", text="")
        r.prop(kmi, "ctrl_ui", icon="EVENT_CTRL", text="")
        r.prop(kmi, "alt_ui", icon="EVENT_ALT", text="")
        r.prop(kmi, "oskey_ui", icon="EVENT_OS", text="")


class ComplexKeybind : 
    def __init__(self, opCls) : 
        if not issubclass(opCls, bl_ops.ComplexKeybindOperator) : 
            raise error.type(opCls, "ComplexKeybindOperator", "ComplexKeybind.__init__")
        self.op = opCls
        self.keys = []
        self.maxlen = 1
        self.onKey = []

        def f(infos) : 
            self.keys.append(infos.value())
            for f in self.onKey : 
                f(self)
        self.op.onKeyEvents.append(f)

        def q() : 
            if len(self.keys)>=self.maxlen : 
                self.keys.clear()
                return True
            return False

        self.op.condsToQuit.append(q)

    def quit(self) : 
        self.keys.clear()

    def setKeymap(self,
                  keyMapsList, 
                  touch, 
                  spaceType = "VIEW_3D", 
                  shift=False, 
                  alt=False, 
                  ctrl=False, 
                  ClsPrefs=None) : 
        newKeyMap(self.op.bl_idname, 
                  keyMapsList, 
                  touch, 
                  spaceType=spaceType, 
                  pshift=shift,
                  palt=alt,
                  pctrl=ctrl,
                  ClsPrefs=ClsPrefs)

    def get(self, keyidx) : 
        if keyidx>= len(self.keys) : 
            return ""

        if self.keys[keyidx] in "0123456789" : 
            return int(self.keys[keyidx])

        return self.keys[keyidx]

    def isNumber(self, keyidx) : 
        try : 
            int(self.keys[keyidx])
            return True
        except : 
            return False


