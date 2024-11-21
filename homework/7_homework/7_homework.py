class Vehicle:
    def __init__(self, name, make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is: {self.name}, from {self.make}, model - {self.model}, {self.year} year ")


class Car(Vehicle):
    def __init__(self, name, make, model, year, fuel_type):
        super().__init__(name, make, model, year)
        self.fuel_type = fuel_type

    def start_endine(self):
        print(f"Car {self.name} start engin on {self.fuel_type}")

    def display_info(self):
        print(
            f"This is: {self.name} car, from {self.make}, model - {self.model}, {self.year} year with {self.fuel_type} Fuel type")


class Boat(Vehicle):
    def __init__(self, name, make, model, year, size, on_the_water=True):
        super().__init__(name, make, model, year)
        self.size = size
        self.on_the_water = on_the_water

    def in_the_ocean(self):
        if self.on_the_water:
            print(f"My {self.name} boat is in the Ocean")
        else:
            print(f"My {self.name} boat is in the garage")

    def display_info(self):
        if self.on_the_water == True:
            water_status = "on the water"
        else:
            water_status = "in the garage"
        print(
            f"This is: {self.size} {self.name} boat, from {self.make}, model - {self.model}, {self.year} year and now it is {water_status} ")


class Scooter(Vehicle):
    def __init__(self, name, make, model, year, charge=100):
        super().__init__(name, make, model, year)
        self.charge = charge

    def charge_level(self):
        if not self.charge > 100 and not self.charge < 0:
            if self.charge >= 80:
                print(f"You can go, charge of {self.name} is full - {self.charge}%")
            elif self.charge >= 30 and self.charge < 80:
                print(
                    f"You can go but be careful, remember to charge it. Charge level of {self.name} - {self.charge}%")
            else:
                print(f"You need to charge your {self.name}, charge is - {self.charge}%")
        else:
            print(f"Something wrong with charge of {self.name} it's {self.charge}%")

    def display_info(self):
        print(
            f"This is: {self.name} scooter, from {self.make}, model - {self.model}, {self.year} year with {self.charge}% charge")


car_1 = Car("First", "BMW", "500", 2000, "Disel")
car_2 = Car("Dream", "Tesla", "X", 2022, "Electric")
boat_1 = Boat("Work", "Yamaha", "WD", 2005, "Big", True)
boat_2 = Boat("Vacation", "WaterD", "7", 2020, "Small", False)
scooter_1 = Scooter("Bolt", "Yamaha", "1", 2015, 99)
scooter_2 = Scooter("Uber", "Yamaha", "2", 2012, 52)
scooter_3 = Scooter("Pyszne", "Dunder", "3", 2011, 25)
scooter_4 = Scooter("Own", "Dunder", "4", 2020, 120)

vehicles = [car_1, car_2, boat_1, boat_2, scooter_1, scooter_2, scooter_3, scooter_4]

for vehicle in vehicles:
    vehicle.display_info()

print("-----------------")
car_1.start_endine()
car_2.start_endine()

print("-----------------")
boat_1.in_the_ocean()
boat_2.in_the_ocean()

print("-----------------")
scooter_1.charge_level()
scooter_2.charge_level()
scooter_3.charge_level()
scooter_4.charge_level()
