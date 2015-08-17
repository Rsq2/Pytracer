from Core.Vector import *
class Object:
    def __init__(self, location):
        self.location = location
        intersects

class Intersection ( Object ):
    def __init__(self, point, obj):
        self.point = point
        self.obj = obj

    def getDistance(self):
        return self.distance


class Sphere( Object ):
    def __init__(self, center, radius, texture):
        self.center = center
        self.radius = radius
        self.texture = texture

    def Intersection(self, ray, t):
        # Constructing a Quadratic Equation
            dist = (ray.origin - self.center)
            a = ray.getDirection() * dist
            b = a * a - dist * dist + self.radius * self.radius

            if b < 0.0: # catch for non-intersection
                return False, t
            t0 = a - sqrt(b)
            t1 = a + sqrt(b)

            returnval = False
            t = 0
            if t1 > 0.1 and t1 < t:
                t = t0
                returnval = True
            elif t1 > 0.1 and t0 < t:
                t = t1
                returnval = True
            return returnval, t

class Ray( Object ):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def getClosestIntersect(ray, objects, t):
        for obj in objects:
            closestIntersect = Vector(0,0,0)
            currentIntersect, t = obj.Intersection(ray, t)
            if currentIntersect > 0.0 and closestIntersect < 0.0:
                closestIntersect = currentIntersect
            elif currentIntersect < closestIntersect:
                closestIntersect = currentIntersect
            return closestIntersect, t

    def cast(self, objects, lights, x, y):
        for obj in World.objects:
            hit = obj.Intersection(self.origin, self.direction)
            
            if hit == False:
                return Ambient()
            else:
                color, reflectFactor, viewRay = reflect(viewRay, obj, t, reflectFactor)
                finalColor += color
            currentDepth += 1


    finalColor = (0.0, 0.0, 0.0) #RGB
    maxDepth = 10
    currentDepth = 0
    reflectFactor = 1
    t = 2000.0

