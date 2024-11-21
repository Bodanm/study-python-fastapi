class Vehicle:
    """Its a base class for Vehicle"""

    def __init__(self, type, color, strenght=100):
        self.type = type
        self.color = color
        self.strenght = strenght

    def move(self):
        print("Your Vehicle is moving")

    def fix(self):
        if self.strenght <= 50:
            print(f"{self.type} is need to be fixed")
        else:
            print(f"Your {self.type} is good")


class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, strenght, cost=0):
        super().__init__(type, color, strenght)
        self.cost = cost

    def move(self):
        print(f"{self.color} {self.type} is moving")
        print(f"Cost of this car is {self.cost}")


class Bicycle(Vehicle):
    def __init__(self, type, color, count_of_wheels, strenght):
        super().__init__(type, color, strenght)
        self.count_of_wheels = count_of_wheels

    def move(self):
        print("You in your bicycle")


car1 = Car("car", 'black', 70, 10000)
car1.move()
car1.fix()

bicycle_1 = Bicycle("Road bike", "blue", 2000, 30)
bicycle_1.move()
bicycle_1.fix()
