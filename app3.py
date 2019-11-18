# Functions
# Tips: - Use them to abstract code that does an specific function
#       - You've to indent the code to let Python know which code is part of the function
#       - Same to variables, name them with lower case and lower brackets between words

def say_hi():
    print("Hi User")


say_hi()


def say_hi_2(name, age):
    print("Hi " + name + " you're " + str(age) + " years old.")


say_hi_2("Pepe", 3)


def number_cube(number):
    return number * number * number


result = number_cube(5)
print(result)


# If Statements
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not a male and not tall")


# Get the max number
def max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print("The max number is: " + str(max_number(4, 5, 10)))
