from abc import ABC, abstractmethod
class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
circle = Circle(3)
print(circle.area())

rectangle = Rectangle(10,20)
print(rectangle.area())