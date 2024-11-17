num = 10
name = "Tom"

# result = num > 5 and name == "Tom"
# result = num < 5 or name == "Tom"
# print(result)

messege = "Tom get some money"
print(name in messege)
print(name not in messege)

name = 'John'
messege = 'You won!'

print(name in messege)
print(name not in messege)

age = 50
name = 'Ira'
pet = 'cat'

print("agenamepet = ", age == 50 and 'I' in name and pet != 'dog')
print("agenamepet = ", age == 50 and 'I' in name or pet == 'dog')