def produce_list(n):
    result = [2**i for i in range(0, n + 1)]
    return result


if __name__ == "__main__":
    result = produce_list(8)
    print(result)
