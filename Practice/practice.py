# @author Dabin Chae
totalShotsMade = 0
totalShotsAttempted = 0
for i in range(1, 4):
    print("Player ", i, ": ")
    shotsMade = int(input("Shots made: "))
    totalShotsMade+= shotsMade
    shotsAttempted = int(input("Shots attempted: "))
    totalShotsAttempted += shotsAttempted

print("Total: ", str(totalShotsMade) + "/" + str(totalShotsAttempted))
percentage = (totalShotsMade / totalShotsAttempted) * 100
print(f"Shooting percentage: {percentage :.3f}%")




