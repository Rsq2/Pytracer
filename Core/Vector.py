from math import sqrt

# Obligatory Vector Object for XYZ Tuples

class Vector( object ):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, int) or (other, float):
            return Vector(self.x * other, self.y * other, self.z * other) 
        elif isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else: 
            return 0 # in case of undefined interactions
        
    def __div__(self, other):
        if isinstance(other, int) or (other, float):
            return Vector(self.x / other, self.y / other, self.z / other) 
        elif isinstance(other, Vector):
            return Vector(self.x / b.x, self.y / b.y, self.z / b.z)
        else: 
            return 0 # in case of undefined interactions

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        
    def unitize(self):
        magnitude = self.magnitude()
        return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)

