#PROJECT TIP CALCULATOR

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? \n$"))
percentage_tip = int(input("What percentage tip would you like to give ? 10, 12, or 15? \n"))
split_bill = int(input("How many people to split the bill? \n"))


total_bill += total_bill * (percentage_tip / 100)
final_bill = round(total_bill / split_bill, 2)

print(f"Each person should pay: ${final_bill}")