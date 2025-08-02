def sum_of_square_of_odd_positive_v2(n):
    result = sum([i * i for i in range(1, n + 1) if i % 2 == 1])
    return result


if __name__ == "__main__":
    result = sum_of_square_of_odd_positive_v2(10)
    print(result)
