def sum_of_n_v2(n):
    summation = sum([i for i in range(1, n + 1)])
    return summation


if __name__ == "__main__":
    result = sum_of_n_v2(100)
    print(result)
