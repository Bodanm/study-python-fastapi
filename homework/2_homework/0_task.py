print("\nNumbers: \n")
num_1 = 5
num_2 = 5.0
num_3 = 10
num_4 = 10.1

print(type(num_1))
print(type(num_2))

print(num_1 == num_2)
print(num_3 == num_4)
print(num_3 < num_4)

print("\nStings:\n")

str_1 = 'water'
str_2 = 'food'

print(type(str_1))

print(str_1 == str_2)
print(str_1 > str_2)
print(str_1 < str_2)

print("\nBools:\n")

bul_1 = True
bul_2 = False

print(type(bul_1))

print(bul_1 == bul_2)
print(bul_1 > bul_2)
print(bul_1 < bul_2)

print("\nLists:\n")

lst_1 = [1, 2, 3]
lst_2 = [1, 2, 4]

print(type(lst_1))

print(lst_1 == lst_2)
print(lst_1 > lst_2)
print(lst_1 < lst_2)

print("\nDictenoris:\n")

dct_1 = {'name': 'Tom', 'surname': 'Kent'}
dct_2 = {'name': 'John', 'surname': 'Kent'}

print(type(dct_1))

print(dct_1 == dct_2)
print(dct_1 != dct_2)

print("\nTuples:\n")

tpl_1 = (1, 2, 3)
tpl_2 = (1, 2, 4)

print(type(tpl_1))

print(tpl_1 == tpl_2)
print(tpl_1 > tpl_2)
print(tpl_1 < tpl_2)

print("\n\n")

print(5 == '5')
