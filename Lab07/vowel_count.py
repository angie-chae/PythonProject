# @author Dabin Chae
# This program will count the number of vowels in user-entered text.

# Get the text
print("Enter some text, and I will count the number of vowels.")
text = input("Text: ")

# Count the number of vowels in the text
vowelCount = 0
for char in text:
    char = char.upper()
    if (char == 'A' or char == 'E' or char == 'I'
        or char == 'O' or char == 'U'):
        vowelCount += 1

# Display the number of vowels
print(f"There are {vowelCount} vowels.")
