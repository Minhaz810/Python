# a = int(input())

# if a < 0:
#     raise ValueError("Value can not be negative")
# b = input("Enter B:")
# if not isinstance(a, float):
#     raise TypeError("Instance must be an integer or float")


def sum(values):
    if not isinstance(values, collections.iterable):
        raise ValueError("Not an iterable")
