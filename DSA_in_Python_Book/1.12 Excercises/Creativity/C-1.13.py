def reverese(li: list):
    start = 0
    end = len(li) - 1

    while start < end:
        temp = li[end]
        li[end] = li[start]
        li[start] = temp

        start += 1
        end -= 1
    return li


if __name__ == "__main__":
    new_list = reverese([1, 2, 3, 4, 5, 6])
    print(new_list)
