import bmesh
class BMesh : 
    def __init__(self, mesh) : 
        self.mesh = mesh
        self.bm = bmesh.new()
        self.bm.from_mesh(mesh)
        self.bm.faces.ensure_lookup_table()
        self.faces = self.bm.faces
        self.edges = self.bm.edges
        self.verts = self.bm.verts

    #you call this when you have finishe your operations on your mesh.
    def finish(self) : 
        self.bm.to_mesh(self.mesh)
        self.bm.free()
        self.bm = None

    def subdivise(self, faces, cuts) : 
        edges = []
        for face in faces : 
            edges.extend(face.edges)

        bmesh.ops.subdivide_edges(self.bm, edges=edges, cuts=cuts, use_grid_fill=True)
        self.bm.faces.ensure_lookup_table()
