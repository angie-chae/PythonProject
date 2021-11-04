# This program displays the break down of caffeine over four
# consecutive 6-hour time periods
# @author Dabin Chae

# Get the caffeine amount (mg)
caffeineIntake = int(input("Amount (mg) of caffeine ingested: "))

# Compute and display caffeine levels
print()
after_six_hrs = caffeineIntake / 2
print(f"After 6 hours: {after_six_hrs:.2f} mg")
after_tweleve_hrs = after_six_hrs / 2
print(f"After 12 hours: {after_tweleve_hrs:.2f} mg")
after_eighteen_hrs = after_tweleve_hrs / 2
print(f"After 18 hours: {after_eighteen_hrs:.2f} mg")
after_one_day = after_eighteen_hrs / 2
print(f"After 24 hours: {after_one_day:.2f} mg")