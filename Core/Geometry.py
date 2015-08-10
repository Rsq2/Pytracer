from Core.Vector import Vector
class Sphere( object ):
    def __init__(self, center, radius, texture):
        self.center = center
        self.radius = radius
        self.texture = texture

    def getCenter(self):
        return self.center
    def getTexture(self):
        return self.texture

    def Intersection(self, ray, t):
        # Constructing a Quadratic Equation
            dist = (ray.origin - self.center)
            a = ray.getDirection() * dist
            b = a * a - dist * dist + self.radius * self.radius

            if b < 0.0: # catch for non-intersection
                return False, t
            t0 = a - sqrt(b)
            t1 = a + sqrt(b)

        #   Evaluating closest intersection using intersection points p0, p1, p2
            returnval = False
            t = 0
            if t1 > 0.1 and t1 < t:
                t = t0
                returnval = True
            elif t1 > 0.1 and t0 < t:
                t = t1
                returnval = True
            return returnval, t


class Ray( object ):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def getStart(self):
        return self.origin

    def getDirection(self):
        return self.direction

class Intersection ( object ):
    def __init__(self, point, obj):
        self.point = point
        self.obj = obj
        self.distance = self.point - obj.center

    def getDistance(self):
        return self.distance

class Light ( object ):
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity
    def getPoint(self):
        return self.point
