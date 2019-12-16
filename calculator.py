def addition(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return  num1 - num2


def multiplication(num1, num2):
    return  num1 * num2


def division(num1, num2):
    return  num1 / num2


num1 = float(input("Enter one number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter the desired operator: ")

if operator == "+":
    print(addition(num1, num2))
elif operator == "-":
    print(substraction(num1, num2))
elif operator == "*":
    print(multiplication(num1, num2))
else:
    print(division(num1, num2))


# Mike's solution
num1 = float(input("Enter one number: "))
operator = input("Enter the desired operator: ")
num2 = float(input("Enter another number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Invalid operator")