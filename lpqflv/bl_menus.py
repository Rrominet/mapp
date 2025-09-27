import bpy
from bpy.app.translations import contexts as i18n_contexts
class VIEW3D_MT_editor_menus(bpy.types.Menu):
    bl_label = ""

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object
        gp_edit = obj and obj.mode in {'EDIT_GPENCIL', 'PAINT_GPENCIL', 'SCULPT_GPENCIL',
                                       'WEIGHT_GPENCIL', 'VERTEX_GPENCIL'}
        ts = context.scene.tool_settings

        layout.menu("VIEW3D_MT_view")

        # Select Menu
        if gp_edit:
            if mode_string not in {'PAINT_GPENCIL', 'WEIGHT_GPENCIL'}:
                if mode_string == 'SCULPT_GPENCIL' and \
                    (ts.use_gpencil_select_mask_point or
                     ts.use_gpencil_select_mask_stroke or
                     ts.use_gpencil_select_mask_segment):
                    layout.menu("VIEW3D_MT_select_gpencil")
                elif mode_string == 'EDIT_GPENCIL':
                    layout.menu("VIEW3D_MT_select_gpencil")
                elif mode_string == 'VERTEX_GPENCIL':
                    layout.menu("VIEW3D_MT_select_gpencil")
        elif mode_string in {'PAINT_WEIGHT', 'PAINT_VERTEX', 'PAINT_TEXTURE'}:
            mesh = obj.data
            if mesh.use_paint_mask:
                layout.menu("VIEW3D_MT_select_paint_mask")
            elif mesh.use_paint_mask_vertex and mode_string in {'PAINT_WEIGHT', 'PAINT_VERTEX'}:
                layout.menu("VIEW3D_MT_select_paint_mask_vertex")
        elif mode_string != 'SCULPT':
            layout.menu("VIEW3D_MT_select_%s" % mode_string.lower())

        if gp_edit:
            pass
        elif mode_string == 'OBJECT':
            layout.menu("VIEW3D_MT_add", text="Add", text_ctxt=i18n_contexts.operator_default)
        elif mode_string == 'EDIT_MESH':
            layout.menu("VIEW3D_MT_mesh_add", text="Add", text_ctxt=i18n_contexts.operator_default)
        elif mode_string == 'EDIT_CURVE':
            layout.menu("VIEW3D_MT_curve_add", text="Add", text_ctxt=i18n_contexts.operator_default)
        elif mode_string == 'EDIT_SURFACE':
            layout.menu("VIEW3D_MT_surface_add", text="Add", text_ctxt=i18n_contexts.operator_default)
        elif mode_string == 'EDIT_METABALL':
            layout.menu("VIEW3D_MT_metaball_add", text="Add", text_ctxt=i18n_contexts.operator_default)
        elif mode_string == 'EDIT_ARMATURE':
            layout.menu("TOPBAR_MT_edit_armature_add", text="Add", text_ctxt=i18n_contexts.operator_default)

        if gp_edit:
            if obj and obj.mode == 'PAINT_GPENCIL':
                layout.menu("VIEW3D_MT_paint_gpencil")
            elif obj and obj.mode == 'EDIT_GPENCIL':
                layout.menu("VIEW3D_MT_edit_gpencil")
                layout.menu("VIEW3D_MT_edit_gpencil_stroke")
                layout.menu("VIEW3D_MT_edit_gpencil_point")
            elif obj and obj.mode == 'WEIGHT_GPENCIL':
                layout.menu("VIEW3D_MT_weight_gpencil")

        elif edit_object:
            layout.menu("VIEW3D_MT_edit_%s" % edit_object.type.lower())

            if mode_string == 'EDIT_MESH':
                layout.menu("VIEW3D_MT_edit_mesh_vertices")
                layout.menu("VIEW3D_MT_edit_mesh_edges")
                layout.menu("VIEW3D_MT_edit_mesh_faces")
                layout.menu("VIEW3D_MT_uv_map", text="UV")
            elif mode_string in {'EDIT_CURVE', 'EDIT_SURFACE'}:
                layout.menu("VIEW3D_MT_edit_curve_ctrlpoints")
                layout.menu("VIEW3D_MT_edit_curve_segments")

        elif obj:
            if mode_string != 'PAINT_TEXTURE':
                layout.menu("VIEW3D_MT_%s" % mode_string.lower())
            if mode_string == 'SCULPT':
                layout.menu("VIEW3D_MT_mask")
                layout.menu("VIEW3D_MT_face_sets")
            if mode_string == "OBJECT" : 
                try : layout.menu("VIEW3D_MT_rig")
                except : pass
                try : layout.menu("VIEW3D_MT_animation")
                except : pass 
        else:
            layout.menu("VIEW3D_MT_object")
            layout.menu("VIEW3D_MT_animation")

class VIEW3D_MT_pivot(bpy.types.Menu):
    bl_label = "Pivot Point"

    def draw(self, context):
        layout = self.layout
        tool_settings = context.tool_settings
        obj = context.active_object
        mode = context.mode

        layout.prop_enum(tool_settings, "transform_pivot_point", value='BOUNDING_BOX_CENTER')
        layout.prop_enum(tool_settings, "transform_pivot_point", value='CURSOR')
        layout.prop_enum(tool_settings, "transform_pivot_point", value='INDIVIDUAL_ORIGINS')
        layout.prop_enum(tool_settings, "transform_pivot_point", value='MEDIAN_POINT')
        layout.prop_enum(tool_settings, "transform_pivot_point", value='ACTIVE_ELEMENT')
        if (obj is None) or (mode in {'OBJECT', 'POSE', 'WEIGHT_PAINT'}):
            layout.prop(tool_settings, "use_transform_pivot_point_align")
        if mode == 'EDIT_GPENCIL':
            layout.prop(tool_settings.gpencil_sculpt, "use_scale_thickness")

class VIEW3D_MT_orientations(bpy.types.Menu):
    bl_label = "Orientation"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="GLOBAL")
        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="LOCAL")
        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="NORMAL")
        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="GIMBAL")
        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="VIEW")
        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="CURSOR")
        layout.prop_enum(scene.transform_orientation_slots[0], "type", value="PARENT")

menus = ( VIEW3D_MT_pivot, 
         VIEW3D_MT_orientations,
         )
