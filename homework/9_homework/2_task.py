from abc import ABC, abstractclassmethod


class Shape(ABC):
    @abstractclassmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def calculate_area(self):
        return 0.5 * self.length * self.height


circle = Circle(5)

rectangle = Rectangle(2, 5)
triangle = Triangle(2, 5)


print(f"Circle area: {circle.calculate_area()}")
print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Triangle area: {triangle.calculate_area()}")


