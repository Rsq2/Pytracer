from Core import *

class Scene ( object ):
    
    def __init__(self, x, y, objects, lights):
        self.x = x
        self.y = y
        self.objects = objects
        self.lights = lights

    def getObjects(self)
        return self.objects
    def getLights(self)
        return self.lights
    def getDimensions(self)
        return self.x, self.y

# Place Objects Into Scene Here
Objects = []
Objects.append( Sphere( Vector( 2, 0, -10), 3, Flat)

Lights = []
Lights.append ( Light( Vector( 5, 10, 0), 1)

World = Scene.new(800,600,Objects[], Lights[])
