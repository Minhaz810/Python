import random

# data = [1, 2, 3, 4, 5, 6]

# random.shuffle(data)


def custom_shuffle(li: list):
    start = 0
    end = len(li) - 1

    for i in li:
        random_1 = random.randint(start, end)
        random_2 = random.randint(start, end)

        temp = li[random_1]
        li[random_1] = li[random_2]
        li[random_2] = temp

    return li


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    modified = custom_shuffle(data)

    print(modified)
