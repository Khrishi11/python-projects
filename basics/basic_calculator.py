# Activity 6: Basic Calculator
# Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.

try: 
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    operation = input("Enter the operation you want to perform (+, -, *, /): ")

    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        result = x / y
    else:
        print("Invalid operation!")

    print("The result is:", result)

except ValueError:
    print("Invalid input! Please enter valid numbers.")
    
