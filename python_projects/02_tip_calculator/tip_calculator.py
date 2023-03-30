print("Welcome to the tip caluculator.")
bill = float(input("What was the total bill? \n $ "))
tip_value = int(input("What percentage tip would you like to give? 10, 12, or 15? \n "))
people = int(input("How many people to split the bill? \n "))
tip = bill / tip_value
total_bill_with_tip = bill + tip
each_pay = (round(total_bill_with_tip / people,2))
print(f"Each person should pay $ {each_pay}")
