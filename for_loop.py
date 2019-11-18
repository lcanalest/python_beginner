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