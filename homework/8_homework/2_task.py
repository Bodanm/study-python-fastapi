from abc import ABC, abstractclassmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def calculate_area(self):
        return 0.5 * self.a * self.h

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


circle = Circle(5)
print(f"Circle area = {circle.calculate_area()}")

triangle = Triangle(2, 5)
print(f"Triangle area = {triangle.calculate_area()}")

rectangle = Rectangle(2, 5)
print(f"Rectangle area = {rectangle.calculate_area()}")
