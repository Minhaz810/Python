def minmax(data):
    min = float("inf")
    max = float("-inf")

    for item in data:
        if item > max:
            max = item
        if item < min:
            min = item
    return max, min


if __name__ == "__main__":
    maximum, minimum = minmax((-12, 25, 30, 35))
    print(minimum)
    print(maximum)
