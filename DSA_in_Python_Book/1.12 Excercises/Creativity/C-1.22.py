def dot_product_of_two_array(a: list, b: list) -> list:
    try:
        if len(a) != len(b):
            raise ValueError("Length of two arrays are not same")
        c = []
        for i in range(len(a)):
            product = a[i] * b[i]
            c.append(product)
        return c

    except ValueError as v:
        return v

    except Exception as e:
        return e


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    b = [6, 5, 4, 3, 2, 1]
    result_array = dot_product_of_two_array(a=a, b=b)
    print(result_array)
