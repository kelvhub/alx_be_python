import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self,lenght: float, width: float):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.width * self.lenght
    
class Circle(Shape):
    def __init__ (self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)