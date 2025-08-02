def generate_values(n):
    res = []
    for i in range(n, n + 40, 10):
        res.append(i)
    return res


if __name__ == "__main__":
    result = generate_values(50)
    print(result)
