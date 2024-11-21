class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        print(self.__dict__)

    def make_sound(self):
        if self.species == "dog":
            print("Haw-haw!")
        elif self.species == "cat":
            print("Nya-nya!")
        else:
            print("I don't know how this animal speaks!")


animal1 = Animal("Tom", "cat", 3)
animal2 = Animal("Bob", "dog", 2)
animal3 = Animal("Sliz", "snake", 20)



animal1.make_sound()
animal2.make_sound()
animal3.make_sound()
