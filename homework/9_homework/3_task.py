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


class Square(Shape):
    def __init__(self, side):
        self.side = side


    def calculate_area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def calculate_area(self):
        return 0.5 * self.length * self.height


circle = Circle(5)

square = Square(2)
triangle = Triangle(2, 5)


shapes = [circle, square, triangle]

for shape in shapes:
    print(shape.calculate_area())


