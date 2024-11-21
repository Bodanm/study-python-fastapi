class Person:
    """Class for creation persons"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attars(self):
        print(f">>>> {self} <<<<")
        print(self.name, self.age)

person1 = Person("Tom", 18)
print(person1)
person1.print_attars()

person2 = Person("Oleg", 50)
print(person2)
person2.print_attars()
