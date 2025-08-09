def count_vowels(s: str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s:
        if i in vowels:
            count += 1

    return count


if __name__ == "__main__":
    vowels = count_vowels("the quick brown fox jumps over the lazy dog")
    print(vowels)
