from lpqflv import bl_bmesh

class Plane : 
    def __init__(self, x=0, y=0, w=0, h=0) : 
        self.x = x
        self.y = y
        self.z = 0
        self.w = w
        self.h = h
        self.d = 0

    def bottom(self) : 
        return self.y + self.h
    
    def right(self) : 
        return self.x + self.w
    
    def collide(self, plane) : 
        # Check if there is a gap along the x-axis
        if self.right() < plane.x or plane.right() < self.x:
            return False
        # Check if there is a gap along the y-axis
        if self.bottom() < plane.y or plane.bottom() < self.y:
            return False
        # No gap along either axis means there is a collision
        return True
        
    #point in a list of 2 floats
    def contains(self, point) : 
        if point[0] < self.x : 
            return False
        elif point[0] > self.right() : 
            return False
        elif point[1] <self.y : 
            return False
        elif point[1] > self.bottom() : 
            return False
        return True

    def draw(self, bm) : 
        verts = []
        verts.append(bm.verts.new((self.x, self.y, 0)))
        verts.append(bm.verts.new((self.right(), self.y, 0)))
        verts.append(bm.verts.new((self.right(), self.bottom(), 0)))
        verts.append(bm.verts.new((self.x, self.bottom(), 0)))
        
        f = bm.faces.new(verts)
        return (verts, f)
        
    def fitIn(self, plane) : 
        if plane.right() > self.right() or plane.x < self.x or plane.y < self.y or plane.bottom() > self.bottom() : 
            return False
        return True

    #return a tuple with 2 tuples of 2 floats (floats a respictvly x and y coords)
    def longestEdge(self) : 
        edge1 = ((self.x, self.y), (self.right(), self.y))
        edge2 = ((self.right(), self.y), (self.right(), self.bottom()))

        dist1 = (edge1[1][0] - edge1[0][0])**2 + (edge1[1][1] - edge1[0][1])**2
        dist2 = (edge2[1][0] - edge2[0][0])**2 + (edge2[1][1] - edge2[0][1])**2

        if dist1 > dist2 : 
            return edge1
        else : 
            return edge2

    #the face is a blender polygon not a bmesh face
    @classmethod
    def fromFace(cls, mesh, face) :
        _r = cls()
        bb = bl_bmesh.boundingBox(mesh, face)
        _r.x = bb[0][0]
        _r.y = bb[0][1]

        _r.w = bb[1][0] - bb[0][0]
        _r.h = bb[1][1] - bb[0][1]

        return _r

    #vertices is a list of vector3 representing the verticles position.
    #they are NOT blender vertices objects.
    @classmethod
    def fromVertices(cls, vertices) :
        _r = cls()
        bb = bl_bmesh.boundingBox(vertices)
        _r.x = bb[0][0]
        _r.y = bb[0][1]

        _r.w = bb[1][0] - bb[0][0]
        _r.h = bb[1][1] - bb[0][1]

        return _r

