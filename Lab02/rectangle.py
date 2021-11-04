# This program displays a rectangle’s area and perimeter based
# upon a user-entered length and width.
# @author Dabin Chae

# Get the length and width
length = int(input("Rectangle length: "))
width = int(input("Rectangle width: "))

# Display the area and perimeter
print()
area = length * width
perimeter = 2 * length + 2 * width
print("Area:", area, "sq units")
print("Perimeter:", perimeter, "units")