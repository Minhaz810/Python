def scale(li: list, factor: int):
    for val in li:
        val *= factor
    return li


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    modified = scale(data, 5)
    print(modified)
    print(data)


"""
val is just a temporary copy of each item in the list (in this case, integers).

val *= factor modifies that temporary variable, not the list itself.
"""
