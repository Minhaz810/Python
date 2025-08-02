def generate_values(n):
    res = []
    for i in range(n, -n - 2, -2):
        res.append(i)
    return res


if __name__ == "__main__":
    result = generate_values(8)
    print(result)
