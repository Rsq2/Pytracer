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
        Object.__init__(self, location)
        self.radius = radius
        self.texture = texture

    def intersection(self, rayOrigin, rayDirection):
        # Constructing a Quadratic Equation
        dist = (self.location - rayOrigin)
        a = rayDirection.normalize() * dist
        b = (self.radius ** 2) - (abs(dist)**2 - a **2)

        if b < 0.0: # Doesn't Intersect
            return False
        
        else:    
            c = a - sqrt(b)
            if <= 0:
                return False
            intersect = rayOrigin + rayDirection.normalize().scale(c)
            return (intersect, self.texture, self)

    def refract_ray(self, rayOrigin, intersect, 


    def normal(self, intersect)
        return (intersect - self.location).normalize()


class Ray( Object ):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def render(self, obj, lights, x, y):    
        hit = obj.Intersection(self.origin, self.direction)
        if hit == False:
            return Ambient()
        intersect, texture, normal = hit
        if intersect == self.origin: # catch for ray going literally nowhere
            return Color(0, 0, 0)
        return texture.computeColor(self.origin, intersect, normal, obj, lights) 

    finalColor = (0.0, 0.0, 0.0) #RGB
    maxDepth = 10
    currentDepth = 0
    reflectFactor = 1
    t = 2000.0

