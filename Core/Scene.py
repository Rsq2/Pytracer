from Core.Geometry import *

class Scene ( object ):

    def __init__(self, x, y, objects, lights):
        self.x = x
        self.y = y
        self.objects = objects
        self.lights = lights

    def getObjects(self):
        return self.objects
    def getLights(self):
        return self.lights
    def getDimensions(self):
        return self.x, self.y
