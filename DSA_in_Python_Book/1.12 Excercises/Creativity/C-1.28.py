def calculate_p_norm(p: int, v: list):
    squared = [(value) ** p for value in v]
    sum_of_squared = sum(squared)

    p_norm = (sum_of_squared) ** (1 / p)

    return p_norm


if __name__ == "__main__":
    result = calculate_p_norm(2, [1, 2, 3, 4, 5])
    print(result)
