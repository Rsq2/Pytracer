from Core.Geometry import *

class Scene ( Object ):

    def __init__(self, objects, lights):
        self.objects = objects
        self.lights = lights

    def getObjects(self):
        return self.objects
    def getLights(self):
        return self.lights
