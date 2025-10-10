class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y 
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def print_vector(self):
        print(f"X is {self.x}, Y is {self.y}")
v1 = Vector(1,3)
v2 = Vector(5,10)
v3 = v1+v2
v3.print_vector()