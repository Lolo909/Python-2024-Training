
# Task 2: Create an abstract class called Shape with an abstract method area.
# Implement two concrete subclasses, Circle and Rectangle, that inherit from Shape.
# Calculate and return the area for both a circle and a rectangle in their respective classes.

from abc import ABC, abstractmethod
import math as math

class Shape(ABC):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, shape, color, radius):
        Shape.__init__(self, shape, color)
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

class Rectangle(Shape):
    def __init__(self, shape, color, width, length):
        Shape.__init__(self, shape, color)
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length

circle = Circle("circle", "blue", 3)
rectangle = Rectangle("rectangle", "green", 2,3)

print("{:.2f}".format(circle.area()))
print(rectangle.area())
