import math 


class Point : 
    def __init__(self, x=0, y=0) : 
        self.x = x
        self.y = y

    #multiply
    def m(val) : 
        self.x*=val
        self.y*=val

    #t muwt be in 0 and 1
    @staticmethod
    def lerp(p1, p2, t) : 
        _r = Point()
        _r.x = (1-t)*p1.x + t*p2.x
        _r.y = (1-t)*p1.y + t*p2.y
        return _r

def bezier(p1, p2, p3, p4, time) : 
    b1 = Point.lerp(p1, p2, time)
    b2 = Point.lerp(p2, p3, time)
    b3 = Point.lerp(p3, p4, time)

    c1 = Point.lerp(b1, b2, time)
    c2 = Point.lerp(b2, b3, time)

    res = Point.lerp(c1, c2, time)
    return res.y

