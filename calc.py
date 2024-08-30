print("Welcome to the Simple Calculator Program!")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

try:
    firstNumber = float(input("Enter the first number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    secondNumber = float(input("Enter the second number: "))

    if operation in operations:
        res = operations[operation](firstNumber, secondNumber)
    else:
        res = "Invalid operation"
except ValueError:
    res = "Error: Invalid input. Please enter numeric values."

print("Result:", res)
