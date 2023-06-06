import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of guesses
max_guesses = 10
num_guesses = 0

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Game loop
while num_guesses < max_guesses:
    # Get the player's guess
    guess = int(input("Take a guess: "))

    # Increase the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        print("Number of guesses:", num_guesses)
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

# Check if the player has used all the guesses
if num_guesses == max_guesses:
    print("Game over! You have used all your guesses.")
    print("The secret number was:", secret_number)
