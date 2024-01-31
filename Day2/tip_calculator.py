print('Welcome to the tip calculator')
total = float(input("What was the total bill? $"))
tip_pct = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round((total + tip_pct * total) / people, 2):.2f}")