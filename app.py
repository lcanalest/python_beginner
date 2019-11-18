# Hello world!
print("Hello world!")
print("Hello \"world\"!")
print("Hello\nworld!")

# Variables
character_name = "Pepe"
character_age = "35"

print("My name is " + character_name + ", ")
print("I'm " + character_age + " years old.")

# Working with strings
phrase = "Chicken Academy"
my_number = 7
print(phrase.lower())
print(phrase.upper())
print(phrase[2:]) # slicing que funciona como substring
print(phrase[2:-1]) # slicing que funciona como substring
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase.index("Ch"))
print(phrase.replace("Ch", "Po"))
print(str(my_number) + " is my favorite number")

# Working with numbers
print(2 + 3)
print(2 * 3)
print(15 / 3)
print(15 - 3)
print(15 / (3 + 4))
print(10 % 3)
print(abs(-4))
print(pow(9, 2))
print(round(9.72))

from math import *
print(sqrt(9))
print(floor(8.7))
print(ceil(3.1))

# Getting input from users
user_name = input("Enter your name: ")
print("Hello " + user_name)

# Basic calculator for sums
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print("The result of your sum is: " + str(result))

# Lists (arrays)
friends = ["Hugo", "Paco", "Luis", "Donald", "Daysi"]
print(friends[0])
print(friends[-1]) # Shows the last item
print(friends[2:]) # Shows the items from the index 2 to the end of the list
print(friends[2:4]) # Shows the items from the index 2 to the index 3, not considering index 4

# Lists Functions
lst_friends = ["Hugo", "Paco", "Luis", "Donald", "Daysi"]
lst_numbers = [42, 13, 56, 41, 4]

lst_friends.extend(lst_numbers) # Copy list lst_numbers to lst_friends
print(lst_friends)

lst_friends_2 = lst_friends.copy()
print(lst_friends_2)
