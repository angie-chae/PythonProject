# This program displays a circle’s area, circumference, and
# volume based upon a user-entered radius.
# @author Dabin Chae

# Get the radius
radius = float(input("Circle radius: "))
# Compute and display the area, circumference, and volume
print()

pi = 3.14159265359
area = pi * radius **2
circumference = pi * radius * 2
volume = 4/3 * pi * radius **3

print("Area:", round(area, 2), "sq units")
print("Circumference:", round(circumference, 2), "units")
print("Volume:", round(volume, 2), "cubic units")