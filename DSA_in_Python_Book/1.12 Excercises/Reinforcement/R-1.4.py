def sum_of_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


if __name__ == "__main__":
    result = sum_of_n(100)
    print(result)
