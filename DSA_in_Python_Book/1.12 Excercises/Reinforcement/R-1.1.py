def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    result = is_multiple(69, 3)
    print(result)
