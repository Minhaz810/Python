amount_charged = int(input("Enter the amount charged: "))
amount_given = int(input("Enter the amount given: "))

list_of_bills = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]


def make_changes(amount_charged, amount_given, list_of_bills):
    change = amount_given - amount_charged

    list_of_bills = sorted(list_of_bills, reverse=True)

    changed_bills = []
    for bill in list_of_bills:
        while change >= bill:
            if bill > change:
                break
            else:
                change -= bill
                changed_bills.append(bill)
    return changed_bills


if __name__ == "__main__":
    changes = make_changes(
        amount_charged=amount_charged,
        amount_given=amount_given,
        list_of_bills=list_of_bills,
    )

    print(changes)
