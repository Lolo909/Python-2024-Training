# Task 2: Create a base class Shape with an attribute color and a method area that returns 0. 
# Then, create two subclasses, Circle and Rectangle, that inherit from the Shape class.
#  Override the area method in each subclass to calculate and return the area of a circle and rectangle, respectively.
#  Create instances of both Circle and Rectangle and call their area methods.
import math as math

class Shape:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, shape, color, radius):
        Shape.__init__(self, shape, color)
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

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

