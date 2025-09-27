import bpy
from lpqflv import bl_UIList
from lpqflv import bl_utils

ADD = 1
REMOVE = 2
REPLACE = 3
DUPLICATE = 4
MOVE = 5
CLEAR = 6            
UNIQUE = 7            

data = []
types = []
listsNb = 0

def typeExists(type) :
    global types
    for t in types : 
        if t["type"] == type : 
            return True
    return False

def _manageExecute(self, bl_prop, activeIdx) :
    if self.action == ADD :
        def f(o) : 
            add(bl_prop, o)
        bl_utils.execOnSelectedObjects(f)
    elif self.action == REMOVE :
        def f(o) : 
            try : 
                remove(bl_prop, o)
            except :
                pass
        bl_utils.execOnSelectedObjects(f)

    elif self.action == CLEAR :
        bl_prop.clear()

    return {'FINISHED'}

class TEMPLATE_UL_PropList(bl_UIList.UIList) :
    def drawItem(self, context, layout, item) : 
        r = layout.row()
        try : 
            icon = item.o.type.upper() + "_DATA"
            r.label(text=item.o.name, icon=icon, translate=False)
        except :
            r.label(text=item.o.name, translate=False)

class List : 
    def __init__(self, colpropname, activeidxpropname) : 
        self.col = colpropname
        self.idx = activeidxpropname
        self.opId = ""
    
    def blProp(self, instance) : 
        return getattr(instance, self.col)

    def activeIdx(self, instance) :
        return getattr(instance, self.idx)
    
    def draw(self, instance, layout) : 
        r = layout.row()
        c1 = r.column(align=True)
        bl_UIList.draw("TEMPLATE_UL_PropList", c1, instance, self.col, self.idx)
        c2 = r.column(align=True)
        ops = c2.operator(self.opId, icon="ADD")
        ops.action = ADD
        ops.instance = instance.name
        ops = c2.operator(self.opId, icon="REMOVE")
        ops.action = REMOVE
        ops.instance = instance.name
        ops = c2.operator(self.opId, icon="X")
        ops.action = CLEAR
        ops.instance = instance.name
    
def list(bltype, colvarname, listElmtType, uiOps=True) : 
    global types

    cls = None
    if not typeExists(listElmtType) :
        class _ptr(bpy.types.PropertyGroup) : 
            o : bpy.props.PointerProperty(type=listElmtType, options={"LIBRARY_EDITABLE"})

        bpy.utils.register_class(_ptr)
        cls = _ptr
    else : 
        for t in types : 
            if t["type"] == listElmtType : 
                cls = t["cls"]
                break

    idxName = colvarname + "_active_idx"
    createActiveIdxProp(bltype, idxName)

    col = bpy.props.CollectionProperty(type=cls, options={"LIBRARY_EDITABLE"}, override = {"LIBRARY_OVERRIDABLE", "USE_INSERTION"})
    setattr(bltype, colvarname, col)
    types.append({"cls" : cls, "type" : listElmtType})

    l = List(colvarname, idxName)
    if uiOps : 
        id = "props.manage_list_prop_" + bltype.bl_rna.name.lower() + "_" + colvarname
        l.opId = id

        class ManageListProp(bpy.types.Operator) :
            bl_idname = id 
            bl_label = ""
            action : bpy.props.IntProperty()
            instance : bpy.props.StringProperty()

            def execute(self, ctx) : 
                instance = bl_utils.blendDataCollectionFromTypeStr(bltype.bl_rna.name)[self.instance]
                return _manageExecute(self, getattr(instance, colvarname), getattr(instance, idxName))

        bpy.utils.register_class(ManageListProp)
    return l

def createActiveIdxProp(bl_prop_collection_parent_type, activeIdxPropName) :
    setattr(bl_prop_collection_parent_type, activeIdxPropName, bpy.props.IntProperty())

def add(bl_prop, o) : 
    tmp = bl_prop.add()
    tmp.o = o

def remove(bl_prop, o) : 
    for i in range(len(bl_prop)) : 
        if bl_prop[i].o == o : 
            bl_prop.remove(i)
            return
    raise Exception("Object not found.")

def get(bl_prop, name) : 
    if type(name) is int :
        return bl_prop[name].o

    for i in range(len(bl_prop)) : 
        if not bl_prop[i].o :
            continue
        if bl_prop[i].o.name == name : 
            return bl_prop[i].o

    raise Exception("Object with name '" + name + "' not found.")

def find(bl_prop, name) : return get(bl_prop, name)

#name could be a name string or a blender object directly
def has(bl_prop, name) : 
    if type(name) is str : 
        try : 
            get(bl_prop, name)
            return True
        except : 
            return False
    else :
        for i in range(len(bl_prop)) : 
            if bl_prop[i].o == name : 
                return True
        return False

def makeUnique(bl_prop) :
    tmp = []
    for i in range(len(bl_prop)) : 
        if not bl_prop[i].o :
            continue
        if bl_prop[i].o not in tmp : 
            tmp.append(bl_prop[i].o)

    bl_prop.clear()
    for _o in tmp : 
        add(bl_prop, _o)

def register() : 
    bpy.utils.register_class(TEMPLATE_UL_PropList)

def unregister() :
    bpy.utils.unregister_class(TEMPLATE_UL_PropList)
