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

def getClosestIntersect(ray, objects):
    closestIntersect = (Vector(0.0,0.0,0.0)
    for obj in objects:
        currentIntersect = obj.Intersection(ray)
        if currentIntersect > 0.0 and closestIntersect < 0.0
            closestIntersect = currentIntersect
        elif currentIntersect < closestIntersect
            closestIntersect = currentIntersect        
        return closestIntersect        
# set ray start z way back to assure intersection

def getNormal(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

def detectIntersection(self, ray, t):
    # Constructing a Quadratic Equation
        dist = (Vector(ray.origin) - Vector(self.center))
        a = Vector(ray.direction).normalize() * dist
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
# TODO: What the function, Batman!

def scan(x, y):
    for num in range(x):
    print num
        for num in range(y):
            finalColor = (0.0, 0.0, 0.0) #RGB
            maxDepth = 10
            currentDepth = 0
            reflectFactor = 1

            # Set ray start depth WAY back to assure intersection
            viewRay = Ray( Vector(x, y, -1000.0), Vector(0, 0, 1.0) )
            
            while currentDepth < maxDepth or 0 < reflectFactor:
                for obj in Objects[]:

                    getClosestIntersect(, Objects[])
                    for light in Lights[]
                        if shadowTest(light, closestInt, obj) == False
                            finalColor = finalColor + computedColor * reflectFactor
                            reflectFactor = reflectFactor * reflectance
                            img.putpixel(finalColor)
                            currentDepth += 1
