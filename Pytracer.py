import Image
import math
from Core.Geometry import *
from Core.Texture import *
from Core.Vector import *

import pdb

class Camera( Object ):
    def __init__(self, location, direction):
        Object.__init__(self, location)
        self.direction = direction
        self.width = 192
        self.height = 108

    def scan(self, objects, lights):
        image = Image.new("RGB", (self.width, self.height), tuple(Ambient()))
        for currentX in range(self.width):
            for currentY in range(self.height):
                viewRay = Ray(Vector(currentX, currentY, -1), self.direction).render(objects, lights)
                image.putpixel((currentX, currentY), tuple(viewRay))
        image.save("trace.png", "png")

# Place Objects Into Scene Here
class Ambient( Color ):
    def __init__(self):
        Color.__init__(self, 0, 0, 0)

if __name__ == "__main__":
    objects = []
    objects.extend((
        Sphere(
            Vector(2, 0, -10), 2.0,
            Diffuse(Color(25, 25, 255), .25)),

        Sphere (
            Vector(-2, -5, -8), 3,
            Diffuse(Color(255, 25, 25), .25))
    ))

    lights = []
    lights.extend((
        Light(
            Vector(-5, 10, 0), Color(200, 255, 200), 2),
        Light(
            Vector(0, 10, -10), Color(200, 200, 255), 10)
    ))

    camera = Camera( (Vector(0, 0, 0)), Vector(0, 0, 1))
    camera.scan(objects, lights)
