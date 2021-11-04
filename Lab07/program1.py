# @author Dabin Chae
# This program will allow a user to guess a number

# Set an integer to guess
number_to_guess = 9

# Set userGuess and numGuesses to 0
userGuess = 0
numGuesses = 0

# Loop while the number is not guessed
while (userGuess != number_to_guess):
    # Get the number to guess and track the number of guesses taken
    userGuess = int(input("Guess a number between 1 and 10: "))
    numGuesses += 1
    # Display if the guess was too low, too high, or correct
    if (userGuess < number_to_guess):
        print("Too low!")
    elif (userGuess > number_to_guess):
        print("Too high!")
    else:
        print("Correct!")
        # Display the number of guesses taken
        print(f"It took you {numGuesses} guesses.")