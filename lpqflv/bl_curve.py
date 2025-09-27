import bpy 
import bmesh

def selectedVerticesWorldPosition() : 
    ob = bpy.context.object
    points = []
    wm = ob.matrix_world
    for spline in ob.data.splines : 
        for bp in spline.bezier_points : 
            if bp.select_control_point : 
                points.append(wm @ bp.co)

    return points

