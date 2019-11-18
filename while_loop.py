# While Loop
i = 1

while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# Secret word!
secret_word = "sabueso"
guess = ""
guess_count = 0
guess_limit = 3

guess = input("Enter your word: ")
while guess_count < guess_limit:
    guess_count += 1
    if guess == secret_word:
        print("You win!")
        exit()
    elif guess != secret_word and guess_count < guess_limit:
        guess = input("Enter another word: ")
    else:
        print("You lose!")


