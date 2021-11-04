# This program displays calories burned given an age, weight,
# heart rate, and time.
# @author Dabin Chae

# Get the age, weight, heart rate, and time
age = int(input("Age: "))
weight = int(input("Weight: "))
heartRate = int(input("Heart Rate: "))
time = int(input("Time in minutes: "))

# Compute and display male and female calories
maleCalories = (age * 0.074 - weight * 0.05741 + heartRate 
* 0.4472 - 20.4022) * time / 4.184

femaleCalories = (age * 0.2017 + weight * 0.09036 + heartRate
* 0.6309 - 55.0969) * time / 4.184

print()
print("Male calories burned:", round(maleCalories, 2))
print("Female calories burned:", round(femaleCalories, 2))