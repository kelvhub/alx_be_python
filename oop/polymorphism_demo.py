import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, lenght: float, height: float):
        self.lenght = lenght
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__ (self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)