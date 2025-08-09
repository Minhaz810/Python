import string


def remove_punctuations(s: str):
    punc = string.punctuation
    s2 = ""
    for i in s:
        if i in punc:
            continue
        else:
            s2 += i
    return s2


if __name__ == "__main__":
    new_string = remove_punctuations("Let's try, Mike.")
    print(new_string)
