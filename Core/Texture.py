class Texture:
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

class Diffuse ( Texture ):
    def __init__(self,
    color = (255, 0, 0)
    reflectance = 100
    opacity = 1

class Specular ( Texture ):

class Transparent ( Texture ):

class Checkers ( Texture ):

