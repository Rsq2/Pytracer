import math
from PIL import Image
from Core import *

#TODO:

#ABSTRACT:
#===========================================================================
#for each pixel on the screen
#    final color = (0, 0, 0)
#    castray from starting point, direction
#    iterate
#        for each object on the screen
#            determine closest ray object and intersection
#        if intersection exists
#            for each light on the screen
#                if the light is not in the shadow of another object
#                    add this light's contriibution to the computed color
#
#    final color = final color + computed color * previous reflection factor
#    reflection factor - reflection factor * surface reflection property
#    increment depth until reflection factor = 0 or maximum depth is reached
#============================================================================

def getClosestIntersect(ray, objects, t):
    closestIntersect = (Vector(0.0,0.0,0.0)
    for obj in objects:
        currentIntersect, t = obj.Intersection(ray, t)
        if currentIntersect > 0.0 and closestIntersect < 0.0
            closestIntersect = currentIntersect
        elif currentIntersect < closestIntersect
            closestIntersect = currentIntersect
        return closestIntersect, t

def getNormal(v1, v2)
    return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

def checkShadows(intersect, norm)
    Lights[] = Scene.getLights()
    for light in Lights[]:
        distance = getNormal(light.getDistance(), intersect)
        if norm * distance <= 0.0:
            continue
        a = math.sqrt(distance * distance)
        if a <= 0.0:
            continue
        childRay = Ray(newStart, distance * (1 \ a ))

        isShadowed == False
        isIntersecting, a = getClosestIntersect(childRay, Objects[])

        if isIntersecting == True:
            isShadowed == True
            break
        return isShadowed

def reflect(ray, obj, t, reflectFactor):
    newStart = ray.getStart() + ray.getDirection() * t
    normal = getNormal(newStart, obj)
    temp = normal * normal
    if temp == 0.0
        break
    temp = 1.0 / math.sqrt(temp)
    normal = normal * temp

    currentTexture = obj.getTexture()
    if currentTexture = None:
        break

    shadowed = testLights(newStart, normal)
    if shadowed == False
        lambert = (ray.getDirection() * normal) * reflectFactor)
        color = obj.getTexture().getColor()
        color = color * lambert

        reflectFactor = reflectFactor * reflectance
        return color, reflectFactor, childRay

def scan(x, y):
    for num in range(x):
    print num
        for num in range(y):
            finalColor = (0.0, 0.0, 0.0) #RGB
            maxDepth = 10
            currentDepth = 0
            reflectFactor = 1
            t = 2000.0

            # Set ray start depth WAY back to assure intersection
            viewRay = Ray( Vector(x, y, -1000.0), Vector(0, 0, 1.0) )

            while currentDepth < maxDepth or 0 < reflectFactor:
                for obj in World.objects:
                    hit, t = getClosestIntersect(viewRay, Objects[])

                    if hit == False:
                        break
                    else:
                        color, reflectFactor, viewRay = reflect(viewRay, obj, t, reflectFactor)
                        finalColor += color
                    currentDepth += 1
            img.putpixel(finalColor)

