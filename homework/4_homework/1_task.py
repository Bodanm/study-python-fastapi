lst = [5, 6, 7, 5, 8]
print(lst)

lst.append(10)
lst.append(20)
print(lst)

lst.remove(10)
print(lst)

sum = 0
for i in lst:
    sum += i

print(sum)

c = 0
while c < len(lst):
    lst[c] *= 2
    c += 1

print(lst)
