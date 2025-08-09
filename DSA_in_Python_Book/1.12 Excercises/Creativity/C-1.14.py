def odd_product_of_pairs(li: list):
    pairs = []
    for i in range(len(li) - 1):
        for j in range(1, len(li)):
            if (li[i] * li[j]) % 2 == 1:
                pairs.append((li[i], li[j]))
    return pairs


if __name__ == "__main__":
    result = odd_product_of_pairs([1, 2, 3, 4, 5, 6])
    print(result)
