def is_distinct_number(li: list):
    if li == list(set(li)):
        return True
    return False


if __name__ == "__main__":
    result = is_distinct_number([1, 2, 3, 4, 4])
    print(result)
