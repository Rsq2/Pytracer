import math
from PIL import Image 


#TODO:


#ABSTRACT:
#===========================================================================
#for each pixel on the screen
#    final color = 0
#    castRay from starting point, direction
#    iterate
#        for each object on the screen
#            determine closest ray object and intersection
#        if intersection exists < -----------------------------[YOU ARE HERE]
#            for each light on the screen
#                if the light is not in the shadow of another object
#                    add this light's contriibution to the computed color
#
#    final color = final color + computed color * previous reflection factor
#    reflection factor - reflection factor * surface reflection property
#    increment depth until reflection factor = 0 or maximum depth is reached
#============================================================================

class Coordinates( object ):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def dotproduct(self, b): 
        return (self.x * b.x, self.y * b.y, self.z * b.z)
    
    def crossproduct(self, b):
        return ((self.y * b.z) - (self.z * b.z), (self.x * b.z) - (self.z * b.x), (self.x * b.y) - (self.y * b.x))
        
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        
    def normalize(self):
        magnitude = self.magnitude()
        return Coordinates((self.x / magnitude), (self.y / magnitude), (self.z / magnitude))
    
    # method overrides so we can add / subtract / multiply / divide our vector and color tuples
    def __add__(self, b):
        return Coordinates(self.x + b.x, self.y + b.y, self.z + b.z)
    def __sub__(self, b):
        return Coordinates(self.x - b.x, self.y - b.y, self.z - b.z)
    def __mul__(self, b):
        return Coordinates(self.x * b.x, self.y * b.y, self.z * b.z)
    def __div__(self, b):
        return Coordinates(self.x / b.x, self.y / b.y, self.z / b.z)
    
class Sphere( object ):
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.texture = color
        
    def Intersection(self, ray):
    # Constructing a Quadratic Equation
        dist = (Coordinates(ray.origin) - Coordinates(self.center))
        a = Coordinates(ray.direction).normalize() * dist
        b = a * a - dist * dist + self.radius * self.radius
        
        if b < 0.0: # catch for non-intersection
            return False
        p1 = a - sqrt(b)
        p2 = a + sqrt(b)
    # Evaluating closest intersection using intersection points p0, p1, p2   
        returnval = False
        p0 = 0
        if p1 > 0.1 and p1 < p:
            p0 = p1
            returnval = True
        elif p2 > 0.1 and p2 < p:
            p0 = p2
            returnval = True
        return returnval        

    def norm(self, n):
        return Coordinates(n - self.center)

class Ray( object ):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    
    def reflect(self, intersection, direction):          
        reflect = 2.0 * (direction * this.normalize())
        newstart = intersection
        newdir = direction - (reflect * this.normalize())
        getClosestIntersect(newstart, newdir)
         
        return # TODO: return color value for incident ray

class Light( object ):
    def __init__(self, center, color, intensity):
        self.center = center
        self.color = color
        self.intensity = intensity

class Intersection ( object ):
    def __init__(self, point, distance, obj):
        self.point = point
        self.distance = distance
        self.obj = obj

def getClosestIntersect(ray, objects):
    closestIntersect = (Coordinates(0.0,0.0,0.0)
    for obj in objects:
        currentIntersect = obj.Intersection(ray)
        if currentIntersect > 0.0 and closestIntersect < 0.0
            closestIntersect = currentIntersect
        elif currentIntersect < closestIntersect
            closestIntersect = currentIntersect        
        return closestIntersect        

def shadowTest(light, intersection, objects):
    


#class World(objects, sky, lights)
    #def __init__(self)
        #self.objects = objects
        #self.sky = sky
        #self.lights = lights

def scan(x, y):
    for num in range(x)
    print num
        for num in range(y):
            finalColor = (0.0, 0.0, 0.0) #RGB
            maxDepth = 10
            currentDepth = 0
            reflectFactor = 1
            while currentDepth < maxDepth or 0 < reflectFactor
                for obj in Objects[] 
                    closestInt = getClosestIntersect(Coordinates(x, y, -1000.0), Objects[])
                    for light in Lights[]
                        if shadowTest(light, closestInt, obj) == False
                            finalColor = finalColor + computedColor * reflectFactor
                            reflectFactor = reflectFactor * reflectance
                            img.putpixel(finalColor)
                            currentDepth += 1
