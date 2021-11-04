# @author Dabin Chae
# This lab program allows a user to view the 
# capital for a given state.

# Display iintroductory message
print("Enter a state, and I will display the capital.")

# Get the state from user
userState = str(input("State: "))
print()

# Compute and display the capital of state
state_capitals = {"Kansas": "Topeka", "California": "Sacramento", "Rhode Island": "Providence", "Colorado": "Denver", "Nebraska": "Lincoln"}

if userState == "Kansas" in state_capitals:
    print("Kansas's capital is", state_capitals["Kansas"] + ".")
elif userState == "California" in state_capitals:
    print("California's capital is", state_capitals["California"] + ".")
elif userState == "Rhode Island" in state_capitals:
    print("Rhode Island's capital is", state_capitals["Rhode Island"] + ".")
elif userState == "Colorado" in state_capitals:
    print("Colorado's capital is", state_capitals["Colorado"] + ".")
elif userState == "Nebraska" in state_capitals:
    print("Nebraska's capital is", state_capitals["Nebraska"] + ".")
else:
    print("I'm sorry, but I still need to record", userState + ".")
    