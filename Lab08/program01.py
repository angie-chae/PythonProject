# @author Dabin Chae
from random import randint

LUCKY_ROLL = 7
NUM_DIE_SIDES = 6
DOUBLE_ROLL = 0
NUM_LUCKY_ROLL = 0

# Get the number of rolls from user
numDiceRolls = int(input("Enter the number of dice rolls: "))

# Roll the dice and both display and count the number of doubles
for i in range(numDiceRolls):
    # Generate, store, and display the two dice values
    diceRoll1 = randint(1, NUM_DIE_SIDES)
    diceRoll2 = randint(1, NUM_DIE_SIDES)
    print(f'{diceRoll1},{diceRoll2}')

    # Tally a double or luck roll
    if diceRoll1 == diceRoll2:
        DOUBLE_ROLL += 1

    if (diceRoll1 + diceRoll2) == LUCKY_ROLL:
        NUM_LUCKY_ROLL += 1

# Display the number of double and lucky rolls
print()
print(f'{DOUBLE_ROLL} double(s) rolled.')
print(f'{NUM_LUCKY_ROLL} lucky roll(s).')