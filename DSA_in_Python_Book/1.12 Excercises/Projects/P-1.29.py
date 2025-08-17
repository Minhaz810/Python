# import itertools


# def form_all_possible_strings(chars: list = []):
#     s = ""
#     li = []
#     for char in chars:
#         s += char
#         all_strings = itertools.permutations(s)
#         for item in all_strings:
#             li.append("".join(list(item)))

#     return li


# if __name__ == "__main__":
#     result = form_all_possible_strings(["c", "a", "t", "d", "o", "g"])
#     print(len(result))
import copy


def form_all_possible_strings(chars: list = []):
    li = []

    def permute(prefix, remaining: list):
        if len(remaining) == 0:
            li.append(prefix)
            return

        for char in remaining:
            new_prefix = prefix + char
            new_remaining = [c for c in remaining if c != char]

            permute(new_prefix, new_remaining)

    permute("", chars)

    return li


if __name__ == "__main__":
    result = form_all_possible_strings(["c", "a", "t", "d", "o", "g"])
    print(result)
