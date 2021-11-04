# @author Dabin Chae

# Get the simple password
simplePassword = input("Simple password: ")

# Modify to make the password stronger
password = ""
for ch in simplePassword:
    if (ch == 'i'):
        password += "!"
    elif (ch == 'a'):
        password += "@"
    elif (ch == 'm'):
        password += 'M'
    elif (ch == 'B'):
        password += '8'
    elif (ch == 'o'):
        password += '.'
    else:
        password += ch

# Append remaining characters and show the modified password
password += "q*s"
print(password)