import bpy 

class RenderFarmProps(bpy.types.PropertyGroup) : 
    jsonStr : bpy.props.StringProperty()

cls = (RenderFarmProps, )

def register() : 
    for c in cls : 
        bpy.utils.register_class(c)
    bpy.types.Scene.lpqflv_renderFarm = bpy.props.PointerProperty(type=RenderFarmProps)

def unregister() : 
    for c in cls : 
        bpy.utils.unregister_class(c)

