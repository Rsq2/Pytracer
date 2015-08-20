from PIL import Image
from Core.Geometry import *
from Core.Texture import *
from Core.Vector import *

class Camera( Object ):
    def init(self, loc, aim, viewPane):
        Object.__init__(self, loc)
        self.width = viewPane[1]
        self.height = viewPane[2]

    def scan(self, objects, lights):
        image = img.new("RGB", (self.width, self.height), tuple(Ambient()))
        for currentX in range(self.width):
            for currentY in range(self.height):
                viewRay = Ray(self.location, Vector(0,0,1.0)).render(objects, lights)
                image.putpixel((currentX, currentY), tuple(viewRay))
        image.save("trace.png", "png")

# Place Objects Into Scene Here
class Ambient(Color):
    def __init__(self):
        Color.__init__(self, 255, 255, 255)

size = [1920, 1080]

objects = []
objects.append(
        Sphere ( Vector(2, 0, -10), 4, (
            Diffuse ((Color(25, 25, 255)), .25))
        )
    )

lights = []
lights.append( 
        Light( Vector( 5, 10, 0), Color(100, 255, 100), 10)
    )

camera = Camera(Vector(0,0,0), Vector(0, 1, 2), size)
camera.scan(objects, lights)
