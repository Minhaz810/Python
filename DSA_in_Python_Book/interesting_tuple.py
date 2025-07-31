data = 1, 2, 3, 4
print(data)


def calculate(x, y):
    s = x + y
    m = x * y

    return s, m


result = calculate(4, 5)
print(type(result))
print(result)


for x, y in [(7, 2), (6, 4)]:
    print(x, y)

my_dict = {"1": "one", "2": "two"}

print(type(my_dict.items()))
