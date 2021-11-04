# @author Dabin Chae
# (No description)

# **Assign an empty list to a variable named labScores
labScores = []

# Get 3 lab scores.
score = float(input("Lab score 1: "))

# ** Use the append method to append the score to the labScores list
labScores.append(score)
score2 = float(input("Lab score 2: "))
# ** Use the append method to append the score to the labScores list
labScores.append(score2)
score3 = float(input("Lab score 3: "))
# ** Use the append method to append the score to the labScores list
labScores.append(score3)

# Display the labScores list COMPLETED
print(labScores)

# Call the sum function with the labScores list and assign the returned
# value to a variable named totalLabScore. COMPLETED
totalLabScore = sum(labScores)

# ** Call the len function with the labScores list and assign the returned
# ** value to a variable named numScores.
numScores = len(labScores)

# ** Use the totalLabScore and numScores variables to compute the  
# ** average score. Assign this value to a variable named average.
average = totalLabScore / numScores

# ** Use an f-string to display "Average Score: {...}" where
# ** ... is replaced with the average formatted to 1 digit of precision.
print(f"Average Score: {average:.1f}")

# ** Call the min function with the labScores list and assign the returned
# ** value to a variable named minLabScore. 
minLabScore = min(labScores)

# Use the index method to asssign the index of minLabScore in the labScores
# list to a variable named minIndex. COMPLETED
minIndex = labScores.index(minLabScore)

# ** Use the pop(i) method to remove the score at minIndex from the labScores
# ** list. You may ignore the score returned from pop.
labScores.pop(minIndex)

# ** Display the current scores in the labScores list
print(labScores)


# ** OPTIONAL (not for extra credit) Again display the average of the scores
# ** in labScores to one digit of precision. Can you do this with one print
# ** statement? That is, do not use any extra variables.
