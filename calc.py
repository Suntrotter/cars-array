def divide(a, b):
    result = a / b
    return result

def multiply(a, b):
    result = a * b
    return result

def subtract(a, b):
    result = a - b
    return result

def add(a, b):
    result = a + b
    return result

option = ''
a = 0
b = 0
def calc(option, a, b):
    option = input("Please enter the operator: ")
    if option != "+" and option != "-" and option != "*" and option != "/":
        print("Invalid operator")
        option = input("Please enter the operator: ")
    a = int(input("Please enter the number: "))
    b = int(input("Please enter the number: "))
    if option == "*":
        print(a, "multiplied by", b, "is", multiply(a, b))
    elif option == "/":
        print(a, "divided by", b, "is", divide(a, b))
    elif option == "-":
        print(a, "minus", b, "is", subtract(a, b))
    elif option == "+":
        print(a, "plus", b, "is", add(a, b))
calc(option, a, b)