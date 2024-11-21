class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(self.__dict__)

    def calculate_area(self):
        return self.width * self.height


rec_1 = Rectangle(10, 10)
rec_2 = Rectangle(2, 5)

print(f"Space of the 1 rectangle is: {rec_1.calculate_area()}, and of the 2 is: {rec_2.calculate_area()}")
