import random
# Generate a random number between 1 and 100
actual_input = random.randint(1, 100)

#  Take the first guess from the user
guess_input = int(input("Guess the number: "))

# Repeat until the guess is correct
while guess_input != actual_input:
    if guess_input < actual_input:
        print(" Guess higher")
    else:
        print(" Guess lower")
    
    # Ask again inside the loop
    guess_input = int(input("Try again: "))

#  When guessed correctly
print(" Correct answer!")
