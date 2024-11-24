class Car:
    def __init__(self, type):
        self.type = type
        self.properties = {}

    def set_properties(self, color, cost, capacity):
        self.properties = {"Color": color, "Cost": cost, "Capacity": capacity}

    def get_properties(self):
        return self.properties


class PetronCar(Car):
    def __init__(self, type):
        self.type = type
        self.properties = {}


car = Car("Toyota")
car.set_properties("Red", 10000, 6)

petrol_car = PetronCar("Volvo")
petrol_car.set_properties("Blue", 5000, 3)

cars = [car, petrol_car]


def get_concret_color_car(color):
    count = 0
    car_types = []
    for car in cars:
        if car.properties["Color"] == color:
            count += 1
            car_types.append(car.type)

    print(f"Count of {color} cars: {count}\nCar type is {car_types}")


get_concret_color_car("Red")
