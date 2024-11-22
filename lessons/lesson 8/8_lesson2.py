from abc import ABC, abstractclassmethod


class Car(ABC):
    def __init__(self, mark, cost):
        self.mark = mark
        self.cost = cost

    @abstractclassmethod
    def car_preview(self):
        pass


class Toyota(Car):
    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")


class Mersedes(Car):
    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")


class BMW(Car):
    def car_preview(self):
        pass


# toyota = Toyota("Crusier", 1000)
# toyota.car_preview()
# mersedes = Mersedes("Quoter", 5000)
# mersedes.car_preview()
#
# bmw = BMW("500", 1000)
# BMW.car_preview()


class Animal(ABC):
    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def eat(self):
        pass


class Cat(Animal):
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def move(self):
        print(f"Cat with {self.color} color movews ahead")

    def eat(self):
        print(f"Cat ate this food for {self.age} years")


class Dog(Animal):
    def __init__(self, distance, type_food):
        self.distance = distance
        self.type_food = type_food

    def move(self):
        print(f"Dog walked {self.distance} km")

    def eat(self):
        print(f"Dog ate {self.type_food} today ")


class AnimalType(Animal):
    pass


class Bird(AnimalType):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"Bird {self.name} fly")

    def eat(self):
        print(f"Bird {self.name} ate 2 days ago ")


cat = Cat("red", 5)
cat.move()
cat.eat()

dog = Dog(5, "meat")
dog.move()
dog.eat()

bird = Bird("Kwin")
bird.move()
bird.eat()

animal_type = AnimalType()
animal_type.move()
animal_type.eat()
