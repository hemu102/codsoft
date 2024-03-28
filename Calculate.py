# Calculator

def calculate():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operator ( +, -, *, / ): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operator. Please enter a valid operator.")
        calculate()

    print(f"Result: {result}")

if __name__ == "__main__":
    calculate()