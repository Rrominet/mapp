import bpy
from lpqflv import bl_ops

class RenderOutput_PT(bl_ops.Operator) : 
    bl_idname = "panels.render_output"
    bl_label = "Render Output"
    bl_description = "Render Output settings"
    okButton = False
    cmds = ["rdoutput", "render_output", "renderOutput"]

    def draw(self, context) : 
        l = self.layout
        l = l.column(align=True)
        l.label(text="Format")
        l.separator()
        l.prop(context.scene.render, "resolution_x")
        l.prop(context.scene.render, "resolution_y")
        l.prop(context.scene.render, "resolution_percentage")
        l.separator()
        l.menu("RENDER_MT_framerate_presets", text=str(context.scene.render.fps) + " fps")
        l.separator()
        l.label(text="Frame Range")
        l.prop(context.scene,"frame_start")
        l.prop(context.scene,"frame_end")
        l.prop(context.scene,"frame_step")
        l.separator()
        l.label(text="Output")

        rd = context.scene.render
        image_settings = rd.image_settings
        l.prop(rd, "filepath", text="")
        l.use_property_split = True
        l.prop(rd, "use_file_extension")
        l.prop(rd, "use_render_cache")

        l.template_image_settings(image_settings, color_management=False)

        if not rd.is_movie_format:
            col = l.column(heading="Image Sequence")
            col.prop(rd, "use_overwrite")
            col.prop(rd, "use_placeholder")

        if image_settings.file_format in {'FFMPEG', 'XVID', 'H264', 'THEORA'} : 
            l.separator()
            self.layout.label(text="Encoding")
            self.draw_encoding(context, self.layout)

    def draw_encoding(self, context, layout) : 
        rd = context.scene.render
        layout.prop(rd.ffmpeg, "format")
        ffmpeg = context.scene.render.ffmpeg
        needs_codec = ffmpeg.format in {
            'AVI',
            'QUICKTIME',
            'MKV',
            'OGG',
            'MPEG4',
            'WEBM',
        }
        if needs_codec:
            layout.prop(ffmpeg, "codec")

        if needs_codec and ffmpeg.codec == 'NONE':
            return

        if ffmpeg.codec == 'DNXHD':
            layout.prop(ffmpeg, "use_lossless_output")

        # Output quality
        use_crf = needs_codec and ffmpeg.codec in {
            'H264',
            'MPEG4',
            'WEBM',
            'AV1',
        }
        if use_crf:
            layout.prop(ffmpeg, "constant_rate_factor")

        # Encoding speed
        layout.prop(ffmpeg, "ffmpeg_preset")
        # I-frames
        layout.prop(ffmpeg, "gopsize")
        # B-Frames
        row = layout.row(align=True, heading="Max B-frames")
        row.prop(ffmpeg, "use_max_b_frames", text="")
        sub = row.row(align=True)
        sub.active = ffmpeg.use_max_b_frames
        sub.prop(ffmpeg, "max_b_frames", text="")

        if not use_crf or ffmpeg.constant_rate_factor == 'NONE':
            col = layout.column()

            sub = col.column(align=True)
            sub.prop(ffmpeg, "video_bitrate")
            sub.prop(ffmpeg, "minrate", text="Minimum")
            sub.prop(ffmpeg, "maxrate", text="Maximum")

            col.prop(ffmpeg, "buffersize", text="Buffer")

            col.separator()

            col.prop(ffmpeg, "muxrate", text="Mux Rate")
            col.prop(ffmpeg, "packetsize", text="Mux Packet Size")

        layout.separator()
        layout.label(text="Audio Encoding")
        layout.use_property_split = True
        layout.use_property_decorate = False

        rd = context.scene.render
        ffmpeg = rd.ffmpeg

        if ffmpeg.format != 'MP3':
            layout.prop(ffmpeg, "audio_codec", text="Audio Codec")

        if ffmpeg.audio_codec != 'NONE':
            layout.prop(ffmpeg, "audio_channels")
            layout.prop(ffmpeg, "audio_mixrate", text="Sample Rate")
            layout.prop(ffmpeg, "audio_bitrate")
            layout.prop(ffmpeg, "audio_volume", slider=True)

class PostProcessing_PT(bl_ops.Operator) : 
    bl_idname = "panels.post_processing"
    bl_label = "Post Processing"
    bl_description = "Post Processing settings"
    okButton = False
    cmds = ["pprocess", "post_processing", "postProcessing"]

    def draw(self, context) : 
        l = self.layout
        l = l.column(align=True)
        l.prop(context.scene.render, "use_compositing")
        l.prop(context.scene.render, "use_sequencer")
        l.prop(context.scene.render, "dither_intensity")

class Opti_PT(bl_ops.Operator) : 
    bl_idname = "panels.opti"
    bl_label = "Optimisation in Viewport"
    okButton = False
    cmds = ["opti", "optimisation"]

    def draw(self, context) : 
        try : 
            bpy.types.OPTIMISATIONS_PT_Scene.draw(self, context)
        except : 
            label(text="Error : optimisation addon not installed.")

class Sampling_PT(bl_ops.Operator) : 
    bl_idname = "panels.sampling"
    bl_label = "Sampling"
    okButton = False
    cmds = ["sample", "sampling"]

    def draw(self, context) : 
        layout = self.layout
        scene = context.scene
        cscene = scene.cycles
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Sampling Viewport")
        heading = layout.column(align=True, heading="Noise Threshold")
        row = heading.row(align=True)
        row.prop(cscene, "use_preview_adaptive_sampling", text="")
        sub = row.row()
        sub.active = cscene.use_preview_adaptive_sampling
        sub.prop(cscene, "preview_adaptive_threshold", text="")

        if cscene.use_preview_adaptive_sampling:
            col = layout.column(align=True)
            col.prop(cscene, "preview_samples", text="Max Samples")
            col.prop(cscene, "preview_adaptive_min_samples", text="Min Samples")
        else:
            layout.prop(cscene, "preview_samples", text="Samples")
        layout.separator()
        layout.label(text="Sampling Render")
        heading = layout.column(align=True, heading="Noise Threshold")
        row = heading.row(align=True)
        row.prop(cscene, "use_adaptive_sampling", text="")
        sub = row.row()
        sub.active = cscene.use_adaptive_sampling
        sub.prop(cscene, "adaptive_threshold", text="")

        col = layout.column(align=True)
        if cscene.use_adaptive_sampling:
            col.prop(cscene, "samples", text="Max Samples")
            col.prop(cscene, "adaptive_min_samples", text="Min Samples")
        else:
            col.prop(cscene, "samples", text="Samples")
        col.prop(cscene, "time_limit")

        row = layout.row(align=True)
        row.prop(cscene, "seed")
        row.prop(cscene, "use_animated_seed", text="", icon='TIME')

class RenderSettings_PT(bl_ops.Operator) : 
    bl_idname = "panels.render_settings"
    bl_label = "Render Settings"
    okButton = False
    cmds = ["rdSettings", "render_settings", "renderSettings"]

    def draw(self, context) : 
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        cscene = scene.cycles

        layout.label(text="Light Paths")
        col = layout.column(align=True)
        col.prop(cscene, "max_bounces", text="Total")

        col = layout.column(align=True)
        col.prop(cscene, "diffuse_bounces", text="Diffuse")
        col.prop(cscene, "glossy_bounces", text="Glossy")
        col.prop(cscene, "transmission_bounces", text="Transmission")
        col.prop(cscene, "volume_bounces", text="Volume")

        col = layout.column(align=True)
        col.prop(cscene, "transparent_max_bounces", text="Transparent")

        layout.separator()
        layout.label(text="Clamping")
        col = layout.column(align=True)
        col.prop(cscene, "sample_clamp_direct", text="Direct Light")
        col.prop(cscene, "sample_clamp_indirect", text="Indirect Light")

        layout.separator()
        layout.label(text="Caustics")
        col = layout.column()
        col.prop(cscene, "blur_glossy")
        col = layout.column(heading="Caustics", align=True)
        col.prop(cscene, "caustics_reflective", text="Reflective")
        col.prop(cscene, "caustics_refractive", text="Refractive")
        layout.separator()
        layout.prop(context.scene.render, "use_motion_blur")
        if (context.scene.render.use_motion_blur) : 
            layout.prop(context.scene.render, "motion_blur_shutter")

        layout.separator()
        layout.label(text="Performance")
        layout.prop(cscene, "use_auto_tile")
        if cscene.use_auto_tile : 
            layout.prop(cscene, "tile_size")
        layout.prop(scene.render, "use_persistent_data")

class ColorManagement_PT(bl_ops.Operator) : 
    bl_idname = "panels.color_management"
    bl_label = "Color Management"
    okButton = False
    cmds = ["colors", "colorManagement", "color_management"]

    def draw(self, context) : 
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        scene = context.scene
        view = scene.view_settings

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=False, even_rows=False, align=True)

        col = flow.column()
        col.prop(scene.display_settings, "display_device")

        col.separator()

        col.prop(view, "view_transform")
        col.prop(view, "look")

        col = flow.column()
        col.prop(view, "exposure")
        col.prop(view, "gamma")
        col.separator()
        col.prop(scene.sequencer_colorspace_settings, "name", text="Sequencer")

        layout.prop(view, "use_curve_mapping")
        if (view.use_curve_mapping) : 
            layout.template_curve_mapping(view, "curve_mapping", type='COLOR', levels=True)

def has_geometry_visibility(ob):
    return ob and (
        (ob.type in {
            'MESH',
            'CURVE',
            'SURFACE',
            'FONT',
            'META',
            'LIGHT',
            'VOLUME',
            'POINTCLOUD',
            'CURVES',
        }) or (ob.instance_type == 'COLLECTION' and ob.instance_collection))

class ObjectVisibility_PT(bl_ops.Operator) : 
    bl_idname = "panels.object_visibility"
    bl_label = "Object Visibility"
    okButton = False
    cmds = ["ovis", "objVis", "objvis", "objectVisibility", "object_visibility"]

    @classmethod 
    def poll(cls, context) : 
        try : 
            return context.object
        except : return False

    def draw(self, context) : 
        layout = self.layout
        layout.use_property_split = True
        ob = context.object
        layout.prop(ob, "hide_select", text="Selectable", invert_checkbox=True, toggle=False)
        col = layout.column(heading="Show In")
        col.prop(ob, "hide_viewport", text="Viewports", invert_checkbox=True, toggle=False)
        col.prop(ob, "hide_render", text="Renders", invert_checkbox=True, toggle=False)

        if has_geometry_visibility(ob):
            col = layout.column(heading="Mask")
            col.prop(ob, "is_shadow_catcher")
            col.prop(ob, "is_holdout")

        layout.separator()
        layout.label(text="Ray Visibility")
        scene = context.scene
        col = layout.column()
        col.prop(ob, "visible_camera", text="Camera")
        col.prop(ob, "visible_diffuse", text="Diffuse")
        col.prop(ob, "visible_glossy", text="Glossy")
        col.prop(ob, "visible_transmission", text="Transmission")
        col.prop(ob, "visible_volume_scatter", text="Volume Scatter")

        if ob.type != 'LIGHT':
            sub = col.column()
            sub.prop(ob, "visible_shadow", text="Shadow")

class ViewportDisplay_PT(bl_ops.Operator) : 
    bl_idname = "panels.viewport_display"
    bl_label = "Viewport Display"
    okButton = False
    cmds = ["vdisp", "viewportDisplay", "viewport_display"]

    @classmethod 
    def poll(cls, context) : 
        try : 
            return context.object
        except : return False

    def draw(self, context) : 
        if context.mode == "POSE" : 
            self.draw_pose(context)
        else :
            self.draw_object(context)

    def draw_pose(self, context) : 
        layout = self.layout
        try :
            bone = context.bone
        except : 
            bone = context.object.data.bones.active
        if not bone : 
            layout.label(text="No active bone.")
            return

        col = layout.column()
        col.prop(bone, "hide", text="Hide", toggle=False)

        ob = context.object
        if not ob:
            return
        pose_bone = ob.pose.bones[bone.name]
        pchan = pose_bone
        col.prop(bone.color, "palette", text="Bone Color")
        col.prop(pose_bone.color, "palette", text="Pose Bone Color")
        layout.separator()
        layout.label(text="Custom Shape")
        col = layout.column()
        col.prop(pchan, "custom_shape")
        if (pchan.custom_shape) : 
            sub = col.column()
            sub.active = bool(pchan and pchan.custom_shape)
            sub.separator()

            sub.prop(pchan, "custom_shape_scale_xyz", text="Scale")
            sub.prop(pchan, "custom_shape_translation", text="Translation")
            sub.prop(pchan, "custom_shape_rotation_euler", text="Rotation")

            sub.prop_search(pchan, "custom_shape_transform",
                            ob.pose, "bones", text="Override Transform")
            sub.prop(pchan, "use_custom_shape_bone_size")

            sub.separator()
            sub.prop(bone, "show_wire", text="Wireframe")

    def draw_object(self, context) : 
        layout = self.layout
        layout.use_property_split = True

        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'VOLUME', 'CURVES', 'POINTCLOUD'})
        has_bounds = (is_geometry or obj_type in {'LATTICE', 'ARMATURE'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_display_type == 'IMAGE')
        is_dupli = (obj.instance_type != 'NONE')
        is_gpencil = (obj_type == 'GPENCIL')

        col = layout.column(heading="Show")
        col.prop(obj, "show_name", text="Name")
        col.prop(obj, "show_axis", text="Axes")

        # Makes no sense for cameras, armatures, etc.!
        # but these settings do apply to dupli instances
        if is_geometry or is_dupli:
            col.prop(obj, "show_wire", text="Wireframe")
        if obj_type == 'MESH' or is_dupli:
            col.prop(obj, "show_all_edges", text="All Edges")
        if is_geometry:
            col.prop(obj, "show_texture_space", text="Texture Space")
            col.prop(obj.display, "show_shadows", text="Shadow")
        col.prop(obj, "show_in_front", text="In Front")
        # if obj_type == 'MESH' or is_empty_image:
        #    col.prop(obj, "show_transparent", text="Transparency")
        sub = layout.column()
        if is_wire:
            # wire objects only use the max. display type for duplis
            sub.active = is_dupli
        sub.prop(obj, "display_type", text="Display As")

        if is_geometry or is_dupli or is_empty_image or is_gpencil:
            # Only useful with object having faces/materials...
            col.prop(obj, "color")

        if has_bounds:
            col = layout.column(align=False, heading="Bounds")
            col.use_property_decorate = False
            row = col.row(align=True)
            sub = row.row(align=True)
            sub.prop(obj, "show_bounds", text="")
            sub = sub.row(align=True)
            sub.active = obj.show_bounds or (obj.display_type == 'BOUNDS')
            sub.prop(obj, "display_bounds_type", text="")
            row.prop_decorator(obj, "display_bounds_type")

        if obj.type == "ARMATURE" : 
            arm = obj.data

            layout.prop(arm, "display_type", text="Display As")

            col = layout.column(heading="Show")
            col.prop(arm, "show_names", text="Names")
            col.prop(arm, "show_bone_custom_shapes", text="Shapes")
            col.prop(arm, "show_bone_colors", text="Bone Colors")

            col = layout.column(align=False, heading="Axes")
            row = col.row(align=True)
            row.prop(arm, "show_axes", text="")
            sub = row.row(align=True)
            sub.active = arm.show_axes
            sub.prop(arm, "axes_position", text="Position")

            sub = col.row(align=True)
            sub.prop(arm, "relation_line_position", text="Relations", expand=True)

 
# add a pivot type panel

class SetPivot(bl_ops.Operator) : 
    bl_idname = "object.set_pivot"
    bl_label = "Set Pivot"
    pivot : bpy.props.StringProperty(name="Pivot", default="INDIVIDUAL_ORIGINS")

    def execute(self, context) : 
        context.scene.tool_settings.transform_pivot_point = self.pivot
        return {'FINISHED'}

# add a snap panel
class Snap_PT(bl_ops.Operator) : 
    bl_idname = "panels.snap"
    bl_label = "Snap"
    bl_description = "Snap settings"
    okButton = False
    cmds = ["snap"]

    def draw(self, context) : 
        tool_settings = context.tool_settings
        obj = context.active_object
        object_mode = 'OBJECT' if obj is None else obj.mode

        layout = self.layout
        layout.prop(tool_settings, "use_snap", text="Enable")
        col = layout.column()

        col.label(text="Snap With")
        row = col.row(align=True)
        row.prop(tool_settings, "snap_target", expand=True)

        col.label(text="Snap To")
        col.prop(tool_settings, "snap_elements_base", expand=True)

        col.label(text="Snap Individual Elements To")
        col.prop(tool_settings, "snap_elements_individual", expand=True)

        col.separator()

        if 'INCREMENT' in tool_settings.snap_elements:
            col.prop(tool_settings, "use_snap_grid_absolute")

        if 'VOLUME' in tool_settings.snap_elements:
            col.prop(tool_settings, "use_snap_peel_object")

        if 'FACE_NEAREST' in tool_settings.snap_elements:
            col.prop(tool_settings, "use_snap_to_same_target")
            if object_mode == 'EDIT':
                col.prop(tool_settings, "snap_face_nearest_steps")

        col.separator()

        col.prop(tool_settings, "use_snap_align_rotation")
        col.prop(tool_settings, "use_snap_backface_culling")

        col.separator()

        if obj:
            col.label(text="Target Selection")
            col_targetsel = col.column(align=True)
            if object_mode == 'EDIT' and obj.type not in {'LATTICE', 'META', 'FONT'}:
                col_targetsel.prop(
                    tool_settings,
                    "use_snap_self",
                    text="Include Active",
                    icon='EDITMODE_HLT',
                )
                col_targetsel.prop(
                    tool_settings,
                    "use_snap_edit",
                    text="Include Edited",
                    icon='OUTLINER_DATA_MESH',
                )
                col_targetsel.prop(
                    tool_settings,
                    "use_snap_nonedit",
                    text="Include Non-Edited",
                    icon='OUTLINER_OB_MESH',
                )
            col_targetsel.prop(
                tool_settings,
                "use_snap_selectable",
                text="Exclude Non-Selectable",
                icon='RESTRICT_SELECT_OFF',
            )

        col.label(text="Affect")
        row = col.row(align=True)
        row.prop(tool_settings, "use_snap_translate", text="Move", toggle=True)
        row.prop(tool_settings, "use_snap_rotate", text="Rotate", toggle=True)
        row.prop(tool_settings, "use_snap_scale", text="Scale", toggle=True)

# add a system to have modifiers settings ? 
# maybe the most commun like Subdivision, Armature, Solidify and Bevel ?

mod_expands = {}

class ExpandMod(bl_ops.Operator) :
    bl_idname = "object.expand_modifier"
    bl_label = "Expand Modifier"
    name : bpy.props.StringProperty(name="Modifier", default="")
    bl_options = {"REGISTER"}

    def execute(self, context) : 
        mod_expands[self.name] = not mod_expands[self.name]
        return {'FINISHED'}


class Mods_PT(bl_ops.Operator) : 
    bl_idname = "panels.mods"
    bl_label = "Modifiers"
    bl_description = "Modifiers settings"
    okButton = False
    width = 400
    cmds = ["mods", "modifiers"]

    def getExpands(self, context) :
        m_names = []
        for m in context.object.modifiers :
            m_names.append(m.name)
            if m.name not in mod_expands :
                mod_expands[m.name] = False
        for key in mod_expands : 
            if key not in m_names : 
                del mod_expands[key]
                break

    def draw(self, context) : 
        self.getExpands(context)
        l = self.layout
        c = l.column()
        for m in context.object.modifiers :
            self.drawModifier(m, c)
        l.separator()
        l.operator("wm.call_menu", text="Add Modifier", icon="ADD").name="OBJECT_MT_modifier_add"

    def drawModifier(self, m, layout) :
        c = layout.box()
        self.drawModHeader(m, c)
        if (mod_expands[m.name]) :
            self.drawModSettings(m, c)

    def drawModHeader(self, m, layout) :
        r = layout.row(align=True)
        r.operator(ExpandMod.bl_idname, text="", icon="DOWNARROW_HLT" if mod_expands[m.name] else "RIGHTARROW_THIN").name = m.name
        r.separator()
        r.prop(m, "name", text="")
        r.prop(m, "show_on_cage", text="")
        r.prop(m, "show_in_editmode", text="")
        r.prop(m, "show_viewport", text="")
        r.prop(m, "show_render", text="")
        r.separator()
        r.operator("object.modifier_apply", text="", icon="CHECKBOX_HLT").modifier=m.name
        r.operator("object.modifier_copy", text="", icon="DUPLICATE").modifier=m.name
        r.operator("object.modifier_move_up", text="", icon="TRIA_UP").modifier=m.name
        r.operator("object.modifier_move_down", text="", icon="TRIA_DOWN").modifier=m.name
        opt = r.operator("object.modifier_move_to_index", text="", icon="ANCHOR_TOP")
        opt.modifier = m.name
        opt.index = 0

        opt = r.operator("object.modifier_move_to_index", text="", icon="ANCHOR_BOTTOM")
        opt.modifier = m.name
        opt.index = len(bpy.context.object.modifiers) - 1

        r.separator()
        r.operator("object.modifier_remove", text="", icon="X").modifier = m.name

    def drawModSettings(self, m, layout) :
        if m.type == "ARMATURE" :
            self.drawArmature(m, layout)
        elif m.type == "SUBSURF" :
            self.drawSubsurf(m, layout)
        elif m.type == "SOLIDIFY" :
            self.drawSolidify(m, layout)
        elif m.type == "BEVEL" :
            self.drawBevel(m, layout)
        elif m.type == "SIMPLE_DEFORM" :
            self.drawDeform(m, layout)
        else : 
            r = layout.row(align=True)
            r.label(text="Not implemented yet.")

    def drawVertexGroup(self, m, layout) :
        r = layout.row(align=True)
        r.prop_search(m, "vertex_group", bpy.context.object, "vertex_groups")
        try :
            r.prop(m, "invert_vertex_group", text="", icon="ARROW_LEFTRIGHT")
        except : 
            pass

    def drawArmature(self, m, layout) : 
        c = layout.column()
        c.prop(m, "object")
        self.drawVertexGroup(m, c)
        c.prop(m, "use_deform_preserve_volume")
        c.prop(m, "use_multi_modifier")
        c.prop(m, "use_vertex_groups")
        c.prop(m, "use_bone_envelopes")

    def drawSubsurf(self, m, layout) : 
        c = layout.column()
        r = c.row(align=True)
        r.prop_enum(m, "subdivision_type", value="CATMULL_CLARK")
        r.prop_enum(m, "subdivision_type", value="SIMPLE")
        c.prop(bpy.context.object.cycles, "use_adaptive_subdivision")
        if not bpy.context.object.cycles.use_adaptive_subdivision :
            c.prop(m, "levels")
            c.prop(m, "render_levels")
        else : 
            c.prop(bpy.context.object.cycles, "dicing_rate")
        c.prop(m, "show_only_control_edges")

    def drawSolidify(self, m, layout) : 
        c = layout.column()
        c.prop(m, "solidify_mode")
        c.prop(m, "thickness")
        c.prop(m, "offset")
        c.prop(m, "use_even_offset")
        c.prop(m, "use_rim")
        c.prop(m, "use_rim_only")
        self.drawVertexGroup(m, c)
        if m.vertex_group : 
            c.prop(m, "thickness_vertex_group")
        c.prop(m, "material_offset")
        c.prop(m, "material_offset_rim")

    def drawBevel(self, m, layout) : 
        c = layout.column()
        r = c.row(align=True)
        r.prop_enum(m, "affect", value="VERTICES")
        r.prop_enum(m, "affect", value="EDGES")
        c.prop(m, "offset_type")
        c.prop(m, "width")
        c.prop(m, "segments")
        c.prop(m, "limit_method")
        c.prop(m, "angle_limit")

    def drawDeform(self, m, layout) : 
        c = layout.column()
        r = c.row(align=True)
        r.prop_enum(m, "deform_method", value="TWIST")
        r.prop_enum(m, "deform_method", value="BEND")
        r.prop_enum(m, "deform_method", value="TAPER")
        r.prop_enum(m, "deform_method", value="STRETCH")

        if m.deform_method == "TWIST" or m.deform_method == "BEND" :
            c.prop(m, "angle")
        elif m.deform_method == "STRETCH" or m.deform_method == "TAPER" :
            c.prop(m, "factor")
        c.prop(m, "object")
        r = c.row(align=True)
        r.prop_enum(m, "deform_axis", value="X")
        r.prop_enum(m, "deform_axis", value="Y")
        r.prop_enum(m, "deform_axis", value="Z")

# ops in not added as command.
ops = (ExpandMod,
       )

cls = (RenderOutput_PT,
       PostProcessing_PT,
       Opti_PT,
       Sampling_PT,
       RenderSettings_PT,
       ColorManagement_PT,
       ObjectVisibility_PT,
       ViewportDisplay_PT,
       Snap_PT,
       Mods_PT,
       )

def register() : 
    for c in ops : 
        bpy.utils.register_class(c)
    for c in cls : 
        bpy.utils.register_class(c)

def unregister() :
    for c in ops : 
        bpy.utils.unregister_class(c)
    for c in cls : 
        bpy.utils.unregister_class(c)
