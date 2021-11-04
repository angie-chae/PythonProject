# This program simulates a simple ATM.
# @author Dabin Chae

# Initial setup
MAX_ATTEMPTS = 3
PIN = '1230'
balance = 1000

# Get the customer's pin
userpin = ""
numAttempts = 0

while (userpin != PIN) and (numAttempts < MAX_ATTEMPTS):
    userpin = input("Enter PIN: ")
    numAttempts += 1

# If successful PIN entry, proceed with menu processing
# otherwise tell customer to reset PIN
print()
if (userpin == PIN):
    # Countinue to present menu and process customer choices
    # until the customer chooses to exit
    menuChoice = '0'
    while (menuChoice != "4"):
        # Display menu and get the customer's choice
        print("(1) Withdraw money")
        print('(2) Deposit money')
        print('(3) Show balance')
        print('(4) Exit')

        menuChoice = input("Your choice: ")
        # Process the choice
        if menuChoice == '1':
            withdrawAmount = float(input("Withdraw amount: $"))
            balance = balance - withdrawAmount
            print()
        elif menuChoice == '2':
            depositAmount = float(input("Deposit amount: $"))
            balance = balance + depositAmount
            print()
        elif menuChoice == '3':
            print(f"Balance: ${balance:,.2f}".format(balance))
            print()
        elif menuChoice == '4':
            print("Have a good day.")
        else:
            print("Invalid choice")
            print()
else:
    print("Maximum attempts reached. You will need to reset your PIN.")