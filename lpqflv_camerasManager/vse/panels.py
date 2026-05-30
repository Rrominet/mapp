import bpy

class _PT_MappStripPanel(bpy.types.Panel) :
    bl_label = "Mapp"
    bl_idname = "_PT_MappStripPanel"
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Strip"

    def draw(self, context) : 
        l = self.layout
        if (not context.active_strip) : return
        if context.active_strip.mapp.type == "none" :
            l.label(text="This strip is not a sequence or a shot.")
            return
        elif context.active_strip.mapp.type == "shot" :
            l.label(text="Shot property : ")
            l.prop(context.active_strip.mapp, "seq")
        elif context.active_strip.mapp.type == "seq" :
            l.label(text="Sequence property : ")
            l.prop(context.active_strip.mapp, "seq_name")
            l.prop(context.active_strip.mapp, "seq_type")
            l.prop(context.active_strip.mapp, "seq_number")

cls = (_PT_MappStripPanel,)

def register() : 
    for c in cls : 
        bpy.utils.register_class(c)

def unregister() : 
    for c in cls : 
        bpy.utils.unregister_class(c)


