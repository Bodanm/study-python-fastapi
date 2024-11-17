num_1 = 5
print(num_1, type(num_1))

num_2 = 3.17
print(num_2, type(num_2))

word = "hello"
print(word, type(word))

check = True
print(check, type(check))

lst_1 = [1, 2, 3]
lst_2 = ['hello', 'my', 'friend']

print(lst_1, type(lst_2))
print(lst_2, type(lst_1))

tpl = (1, 2, 3)
print(tpl, type(tpl))

dct = {'name': 'John', 'age': 23}
print(dct, type(dct))

set_ex = {1, 2, 3, 1}
print(set_ex, type(set_ex))

print(None, type(None))


class Person:
    pass


a = Person()
print(a, type(a))