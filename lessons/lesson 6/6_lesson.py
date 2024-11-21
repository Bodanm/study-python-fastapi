class Person:
    """Class for creation persons"""
    name = 'Tom'
    age = 18
    high = 180

# print(Person.name, Person.age)
# Person.age = 50
# print(Person.name, Person.age)
#
# print(Person.__dict__)

person1 = Person()
person1.is_animal = False
print(person1.__dict__)
print(Person.__dict__)
print(getattr(person1, "name"))
print(getattr(person1, "tall", False))

person1.age=59
person1.color = "white"
print(person1.__dict__)

setattr(person1, "high", 100)
print(person1.__dict__)

print(hasattr(person1, 'name'))
print(hasattr(person1, 'where is'))


del Person.high
print(Person.__dict__)
print(hasattr(Person, 'high'))


delattr(Person, "age")
print(Person.__dict__)
print(hasattr(Person, 'age'))

print(Person.__doc__)