# @author Dabin Chae
# This program that allows a user to enter a 
# starting integer, ending integer, and step size.

# Get input from user
startNumber = int(input("Starting integer: "))
endNumber = int(input("Ending integer: "))
stepSize = int(input("Step size: "))

# Check if stepSize is invalid
if (stepSize >= 0) and (endNumber < startNumber) or (stepSize < 0) and (endNumber > startNumber):
    print("Invalid step size.")
else:
    # Put variables into a for loop, inside the range function
    for i in range(startNumber, endNumber, stepSize):
        # Display the sequence of values
        print(i, end=" ")