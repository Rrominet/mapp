import bpy
if ("Strip" in bpy.types.__dict__):
    bpy.types.Sequence = bpy.types.Strip
from lpqflv_camerasManager.vse import strips
from lpqflv import bl_ui

def updateName(self, ctx) : 
    try : 
        strips.setStripTextFromProps(ctx.active_sequence_strip)
    except : pass

class MappSequenceProps(bpy.types.PropertyGroup) :
    type : bpy.props.EnumProperty(items=[
            ("none", "None", "", 0),
            ("shot", "Shot", "", 1),
            ("seq", "Sequence", "", 2),
        ], name="Type")
    
    children : bpy.props.StringProperty(name="Children", description="Children of this sequence in JSON format")
    seq : bpy.props.StringProperty(name="Sequence", description="Sequence name containing this shot")
    seq_type : bpy.props.EnumProperty(items=bl_ui.items("Animation", "Lighting and Shading", "Render Settings"), default="Animation", name="Type")
    seq_number : bpy.props.IntProperty(name="Sequence Number", description="Sequence number in this movie", default=1, min=0, update=updateName)
    seq_name : bpy.props.StringProperty(name="Sequence Name", update=updateName)

def onAutoUpdate(self, context) : 
    if self.autoUpdate : 
        bpy.app.handlers.depsgraph_update_post.append(strips.updateAllSeqs)
    else :
        bpy.app.handlers.depsgraph_update_post.remove(strips.updateAllSeqs)

class MappSequenceSceneProps(bpy.types.PropertyGroup) :
    autoUpdate : bpy.props.BoolProperty(name="Auto Update", default=True, description="Automaticly update sequence length when the depthgraph is updated.", update=onAutoUpdate)

cls = (MappSequenceProps, MappSequenceSceneProps)

def register() : 
    for c in cls : 
        bpy.utils.register_class(c)
    bpy.types.Sequence.mapp = bpy.props.PointerProperty(type=MappSequenceProps)
    bpy.types.Scene.mapp = bpy.props.PointerProperty(type=MappSequenceSceneProps)

def unregister() : 
    for c in cls : 
        bpy.utils.unregister_class(c)


