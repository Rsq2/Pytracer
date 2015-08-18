from math import sqrt
from Core.Geometry import Object
# Obligatory Vector Object for XYZ Tuples

class Vector( Object ):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError

    def __abs__(self):
        return sqrt(sum(map(lambda x: x**2, list(self))))

    def normalize(self):
        return self.scale(1/abs(self)) 

    def scale(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.x * other.z - self.z * other.x, self. x * other.y - self.y * other.x)

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

class Color:
    def __init__(self, r, g, b, a = 0):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = 0
    def __getitem__(self, i):
        if i == 0:
            return self.r
        elif i == 1:
            return self.g
        elif i == 2:
            return self.b
        elif i == 3:
            return self.a
        else:
            raise IndexError

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)
    def __mul__(self, other):
        if isinstance(other, Color)
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        return Color(self.r * other, self.g * other, self.b * other)
    def __pow__(self, other):
        kapow = map(lambda x: ((x/255)**other)/255, list(self))
        return Color(kapow[0], kapow[1], kapow[2])

    def __div__(self, other):
        return self * (1/other)
