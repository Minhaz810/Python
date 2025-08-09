def scale(li: list):
    for i in range(len(li)):
        li[i] *= 5

    return li


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    modified = scale(data)  # is pointing to the same data list
    data[0] = 100
    print(modified)
    print(data)


"""
Even though integers are immutable, you're not changing the integer object; you're changing which object is stored in the list at each index.

So data[j] = factor means:

"Replace the element at index j in the list data with a reference to the factor object."

This is modifying the list, not modifying the integers inside it (which you couldn’t do, because integers are immutable).
"""
