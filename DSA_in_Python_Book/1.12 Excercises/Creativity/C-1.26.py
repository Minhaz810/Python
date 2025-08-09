def arithmetic_check(a, b, c):
    if a + b == c:
        return "Can be used for addition"
    elif a - b == c:
        return "Can be used for subtraction"
    elif a * b == c:
        return "Suitable for multiplication"
    elif a / b == c:
        return "Suitable for division"
    else:
        return "Not good for any of the big four"


if __name__ == "__main__":
    print(arithmetic_check(1, 2, 3))
    print(arithmetic_check(1, 3, 3))
    print(arithmetic_check(1, 4, 3))
    print(arithmetic_check(3, 1, 3))
    print(arithmetic_check(4, 1, 3))
