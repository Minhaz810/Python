def out_of_buffer(array: list, index: int, value: float):
    try:
        array[index] = value
        return array
    except IndexError as e:
        return "Don't try buffer overflow attacks in python !"


if __name__ == "__main__":
    arr = out_of_buffer(array=[1, 2, 3, 4, 5, 6, 7], index=100, value=100)
    print(arr)
