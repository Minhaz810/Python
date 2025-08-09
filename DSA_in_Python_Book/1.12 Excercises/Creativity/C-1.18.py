def produce_list(n):
    li = [(i * i) + i for i in range(n)]
    return li


def produce_list2(n):
    li = [i * (i + 1) for i in range(n)]
    return li


if __name__ == "__main__":
    li = produce_list(10)
    li2 = produce_list2(10)
    print(li)
    print(li2)
