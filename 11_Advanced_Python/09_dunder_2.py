class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x , self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(45,50)
v2 = Vector(4,6)

v3 = v1 + v2
print(v3)

v4 = v3 - v1
print(v4)

v5 = v4*10
print(v5)