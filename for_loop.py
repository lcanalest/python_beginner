# For loop
word = "Sabueso"
for letter in word:
    print(letter)


friends = ["Hugo", "Paco", "Luis"]
for friend in friends:
    print(friend)


for index in range(len(friends)):
    print(friends[index])


for index in range(5, 10):
    if index == 5:
        print("First iteration")
    else:
        print("Not first iteration")

for index in range(5):
    print(index)


# Exponent function
# Let's try to replicate the result of pow(3, 4), but with a for loop
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

    return result


print(raise_to_power(3, 2))
print(pow(3, 2))


# 2D Lists & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print("Get the first item from the first row: " + str(number_grid[0][0]))

for row in number_grid:
    print(row)

for row in number_grid:
    for column in row:
        print(column)
