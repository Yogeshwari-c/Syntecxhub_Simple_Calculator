def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return "Error: Invalid operator."


def calculator():
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                result = calculate(num1, operator, num2)
                print("Result:", result)

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "2":
            print("Calculator cleared.")

        elif choice == "3":
            print("Thank you for using the calculator!")
            break

        else:
            print("Error: Please choose 1, 2, or 3.")


if __name__ == "__main__":
    calculator()