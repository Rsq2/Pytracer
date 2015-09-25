from Core.Vector import *
from Core.Texture import *
import pdb

class Object:
    def __init__(self, location):
        self.location = location

class Intersection ( Object ):
    def __init__(self, rayOrigin,  obj):
        Object.__init__(self, location)
        self.rayOrigin = rayOrigin
        self.obj = obj

class Sphere( Object ):
    def __init__(self, location, radius, texture):
        Object.__init__(self, location)
        self.radius = radius
        self.texture = texture

    def intersection(self, rayOrigin, rayDirection):
        # Solve for 't'
        dist = self.location - rayOrigin
        a = rayDirection.normalize() * dist
        pdb.set_trace()
        b = (self.radius ** 2) - (abs(dist)**2 - a ** 2)

        if b < 0.0: # Doesn't Intersect
            return False

        else:    
            c = a - sqrt(b)
            if c <= 0.0:
                return False
            intersect = rayOrigin + rayDirection.normalize().scale(c)
            return (intersect, self.texture, self)

    def normal(self, intersect):
        return (intersect - self.location).normalize()

    def shadow(self, intersect, direction):
        return max([direction.normalize() * (intersect - self.location).normalize(), 0])

class Ray( Object ):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def render(self, obj, lights):    
        for each in obj:
            hit = each.intersection(self.origin, self.direction)
            if hit == False:
                return Ambient()
            intersect, texture, normal = hit
            if intersect == self.origin: # catch for ray going literally nowhere
                return Color(0, 0, 0)
            return texture.computeColor(self.origin, intersect, normal, obj, lights)

class Light ( Object ):
    def __init__(self, location, color, intensity):
        Object.__init__(self, location)
        self.color = color
        self.intensity = intensity
