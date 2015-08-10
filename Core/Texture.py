class Texture( object ):
    def __init__(self, reflectance, color, opacity):
        self.reflectance = reflectance
        self.color = color
        self.opacity = opacity
    def getReflectance(self):
        return self.reflectance
    def getColor(self):
        return self.color
    def getOpacity(self):
        return self.opacity

class Flat ( Texture ):
    color = (255, 0, 0)
    reflectance = 100
    opacity = 1

