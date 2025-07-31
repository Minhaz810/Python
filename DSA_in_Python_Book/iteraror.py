import sys

li = [20, 30, 40]

it = iter(li)


print(next(it))
print(next(it))
li[2] = 45
print(next(it))  # refers to the original list, and the list is modified


x = [1, 2, 3]
print(sys.getsizeof(x))
