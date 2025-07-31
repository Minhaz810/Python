def sum_of_square_of_odd_positive(n):
    summation = 0

    for i in range(1, n):
        if i % 2 == 1:
            summation += i * i

    return summation


if __name__ == "__main__":
    result = sum_of_square_of_odd_positive(10)
    print(result)
