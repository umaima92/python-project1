
#calculator
import math
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def exponentiate(num1, num2):
    return num1 ** num2

def square_root(num1):
    if num1 >= 0:
        return math.sqrt(num1)
    else:

        return "Error: Cannot calculate square root of a negative number"

#input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Select an operation (+, -, *, /, ^, sqrt): ")

#calculaton
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
elif operation == '^':
    result = exponentiate(num1, num2)
elif operation == 'sqrt':
    result = square_root(num1)
else:
    print("Invalid operation selected")
if result is not None:
    print("Result:", result)
