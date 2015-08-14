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

    def scale(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

class Color:
    def __init__(self, r, g, b, a = 0):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = 0

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)
    def __mul__(self, other):
        if isinstance(other, Color)
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        return


