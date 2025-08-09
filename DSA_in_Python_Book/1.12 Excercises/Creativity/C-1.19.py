def generate_char(n):
    li = [chr(i) for i in range(97, n + 98)]
    return li


if __name__ == "__main__":
    char_list = generate_char(25)
    print(char_list)
