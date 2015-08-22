from Core.Vector import *
from Core.Geometry import *

class Texture:
    # Null Texture
    def computeColor(self, rayOrigin, intersect, obj, objects, lights):
        return (0, 0, 0)

class Diffuse ( Texture ):
    def __init__(self, color, ambient):
        self.color = color
        self.ambient = ambient
        self.coef = 1-ambient

    def computeColor(self, rayOrigin, intersect, obj, objects, lights):
        finalcolor = Color (0, 0, 0)

        #TODO: Refactor into testLights(texture, ...) with texture.applyLightingModel(hitdata)
        for light in lights:
            newDir = (light.location - intersect).normalize()
            hit = objects.intersection(intersect, newDir, obj)
            if hit is False or abs(intersect - light.location) < abs(intersect - hit):
                
                #TODO: refactor this into applyLightingModel()
                finalcolor += light.color * light.intensity * obj.shadow(intersect, newDir) * self.coef / newDir ** 2
        return finalcolor

#TODO: IMPLEMENT "computeColor" for all these
class Specular ( Texture ):
    pass
class Transparent ( Texture ):
    pass
class Checkers ( Texture ):
    pass

