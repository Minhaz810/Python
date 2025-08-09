lines = []


def print_reverse_line(file_path):
    while True:
        try:
            line = file_path.readline()
            if line == "":
                raise EOFError("End of the file path")
            else:
                lines.append(line)
        except EOFError as e:
            end = len(line) - 1
            for i in range(len(lines)):
                print(lines[end - i])
            return


if __name__ == "__main__":
    file_path = open(
        "/home/minhaz/Projects/Personal/Python/DSA_in_Python_Book/1.12 Excercises/Creativity/C-1.21-file.txt"
    )
    print_reverse_line(file_path=file_path)
