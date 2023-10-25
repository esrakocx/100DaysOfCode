print("Welcome to he tip calculator.")
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_percentage = bill * (tip / 100)
each_bill = (bill + tip_percentage) / people
print(f"Each person should pay: {each_bill:.2f}")