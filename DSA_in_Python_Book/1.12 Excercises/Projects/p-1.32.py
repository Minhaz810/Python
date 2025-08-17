result = float(input("Please enter the first number: "))

while True:
    operator = input("Please enter an operator (+, -, *, /) or = to finish: ")

    if operator == "=":
        print("Final result:", result)
        break

    k = float(input("Please enter another number: "))
    result = eval(f"{result}{operator}{k}")
    print("Current result:", result)
