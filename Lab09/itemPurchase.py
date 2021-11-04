# @author Dabin Chae

# Get the item cost and initial customer deposit
cost = float(input("Vending machine item cost: $"))
deposit = float(input("Please deposit money: $"))

# Get more money until the cost is reached
while (deposit < cost):
    print(f"\n{cost - deposit:.2f} still needed.")
    deposit += float(input("Deposit additional money: $"))

# Tell the user to take the item and any remaining change
print("\nPlease take your item")
change = deposit - cost
if (change > 0):
    print(f"Please take your change of ${change:.2f}")