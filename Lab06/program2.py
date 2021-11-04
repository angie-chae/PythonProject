# @author Dabin Chae
# This lab program will get an x-coordinate (integer)
# and a y-coordinate (integer) from the user.

# Get the coordinates
x_coordinate = int(input("X coordinate? "))
y_coordinate = int(input("Y coordinate? "))

# Display the graph location
if x_coordinate > 0:
    if y_coordinate > 0:
        print("Quadrant I")
    elif y_coordinate < 0:
        print("Quadrant IV")
    else:
        print("X-axis")
elif x_coordinate < 0:
    if y_coordinate > 0:
        print("Quadrant II")
    elif y_coordinate < 0:
        print("Quadrant III")
    else:
        print("X-axis")
else:
    if y_coordinate != 0:
        print("Y-axis")
    else:
        print("Origin")