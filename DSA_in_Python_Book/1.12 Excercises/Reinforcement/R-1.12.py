import random

data = [1, 2, 3, 4, 5, 6]

print(random.choice(data))


def own_choice(data):
    start = 0
    end = len(data) - 1
    random_index = random.randrange(start, end)

    return data[random_index]


if __name__ == "__main__":
    res = own_choice([1, 2, 3, 4, 5, 6])
    print(res)
