class Sphere( object ):
    def __init__(self, center, radius, texture):
        self.center = center
        self.radius = radius
        self.texture = texture 
    def getCenter:
        return self.center
   
   class Ray( object ):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def getStart(self):
        return self.origin

    def getDirection(self):
        return self.direction

    # TODO: Find someplace to implement this
    #def reflect(self, intersection, direction):          
        #reflect = 2.0 * (direction * this.unitize())
        #newstart = intersection
        #newdir = direction - (reflect * this.unitize())
        #getClosestIntersect(newstart, newdir)
         
        #return # TODO: return color value for incident ray

class Intersection ( object ):
    def __init__(self, point, distance, obj):
        self.point = point
        self.obj = obj
        self.distance = self.point - obj.center

    def getDistance
        return self.distance
