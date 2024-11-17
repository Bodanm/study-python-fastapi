num_str = 125
print(num_str, type(num_str))

num_str = str(num_str)
print(num_str, type(num_str))

print()

messege = 'Hi, my name is Python!'
messege = messege.replace('y', '0')
print(messege)
messege = messege.replace('i', '1')
print(messege)

print()

split_test = 'This is a split test'
print(split_test, type(split_test))
split_test = split_test.split(' ')
print(split_test, type(split_test))

string_join = " ".join(split_test)
print(string_join, type(string_join))

print("Len of the string_join is: ", len(string_join))