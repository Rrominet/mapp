import bpy
from lpqflv_camerasManager.vse import ops
from lpqflv_camerasManager.vse import strips

class MappSequencerMenu(bpy.types.Menu):
    bl_idname = "VSE_MT_mapp_editing"
    bl_label = "Mapp Editing"

    def draw(self, context):
        shots = strips.shotsFromSelection()
        seqs = strips.seqsFromSelection()
        sh = strips.shotUnderTheCursor()
        layout = self.layout
        layout.operator_context = "INVOKE_DEFAULT"
        if (sh) : 
            layout.operator(ops.VSE_SetCurrentShotTxt.bl_idname)
        if (shots) : 
            layout.operator(ops.VSE_TransformToShot.bl_idname)
            layout.operator(ops.VSE_TransformToSeq.bl_idname)
            layout.separator()
        if (shots and seqs) : 
            layout.operator(ops.VSE_AddShotsToSeq.bl_idname)
            layout.operator(ops.VSE_LinkShotsToSeq.bl_idname)
            layout.separator()
        layout.operator(ops.VSE_CreateShot.bl_idname)
        layout.operator(ops.VSE_CreateSeq.bl_idname)
        if (seqs) :
            layout.separator()
            layout.operator(ops.VSE_OpenSeq.bl_idname)
        layout.separator()
        layout.prop(context.scene.mapp, "autoUpdate")
        layout.separator()
        layout.operator(ops.VSE_AddReviewToShot.bl_idname)

def register() : 
    bpy.utils.register_class(MappSequencerMenu)
def unregister() : 
    bpy.utils.unregister_class(MappSequencerMenu)
