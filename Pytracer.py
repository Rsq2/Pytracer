import math
from PIL import Image
from Core.Geometry import *
from Core.Texture import *
from Core.Vector import *
from Core.Scene import *

def getNormal(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

def checkShadows(intersect, norm):
    Lights = Scene.getLights()
    for light in Lights:
        distance = getNormal(light.getDistance(), intersect)
        if norm * distance <= 0.0:
            continue
        a = math.sqrt(distance * distance)
        if a <= 0.0:
            continue
        childRay = Ray(newStart, distance * (1 / a ))

        isShadowed == False
        isIntersecting, a = getClosestIntersect(childRay, Objects)

        if isIntersecting == True:
            isShadowed == True
            break
        return isShadowed

def reflect(ray, obj, t, reflectFactor):
    newStart = ray.getStart() + ray.getDirection() * t
    normal = getNormal(newStart, obj)
    temp = normal * normal
    if temp == 0.0:
        reflectFactor = 0
        return reflectFactor
    temp = 1.0 / math.sqrt(temp)
    normal = normal * temp

    currentTexture = obj.getTexture()
    if currentTexture == None:
       reflectFactor = 0
       return reflectFactor

    shadowed = testLights(newStart, normal)
    if shadowed == False:
        lambert = (ray.getDirection() * normal) * reflectFactor
        color = obj.getTexture().getColor()
        color = color * lambert

        reflectFactor = reflectFactor * reflectance
        return color, reflectFactor, childRay

class Camera( Object ):
    def init(self, loc, aim, list(viewPane)):
        Object.__init__(self, loc)
        self.width = viewPane[1]
        self.height = viewPane[2]

    def scan(self, objects, lights):
        image = img.new("RGB", (self.width, self.height), tuple(Ambient()))
        for currentX in range(x):
            for currentY in range(y):
                viewRay = Ray(self.location, Vector(0,0,1.0)).cast(objects, lights)
                image.putpixel(finalColor)

# Place Objects Into Scene Here
class Ambient(Color):
    def __init__(self):
        Color.__init__(self, 255, 255, 255)

#TODO: Implement camera
objects = []
objects.append( Sphere( Vector( 2, 0, -10), 3, Diffuse))

lights = []
lights.append( Light( Vector( 5, 10, 0), 1))

camera = Camera(Vector(0,0,0), Vector(0, 1, 2), (1920, 1080))
camera.scan(objects, lights)
