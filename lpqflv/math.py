import math 
import mathutils

class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

def dist(p1, p2, useSqrt=True) : 
    if not isinstance(p1, Point) : 
        p1 = Point(p1[0], p1[1])
    if not isinstance(p2, Point) : 
        p2 = Point(p2[0], p2[1])

    res = (p2.x - p1.x)**2 + (p2.y - p1.y)**2
    if useSqrt : 
        return math.sqrt(res)
    return res

def dist2(x1, y1, x2, y2, useSqrt=True) : 
    return (Point(x1, y1), Point(x2, y2), useSqrt)

def vectorFromPoints(p1, p2) : 
    if not isinstance(p1, Point) : 
        p1 = Point(p1[0], p1[1])
    if not isinstance(p2, Point) : 
        p2 = Point(p2[0], p2[1])

    return mathutils.Vector((p2.x - p1.x, p2.y - p1.y))

def _3dPointFromMatrix(m) : 
    return [m[0][3], m[1][3], m[2][3]]

def distFromMatrices(m1, m2, useSqrt=True) : 
    p1 = _3dPointFromMatrix(m1)
    p2 = _3dPointFromMatrix(m2)
    res = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2
    if useSqrt : 
        return math.sqrt(res)
    return res
