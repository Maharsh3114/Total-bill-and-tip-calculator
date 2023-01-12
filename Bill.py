# <!-------------------- This is a tip and total bill calculator-------------------!>

print("Welcome to tip calculator")
print("What was the total bill ?")
bill = float(input())
print("What percentage of tip would you like to give ? 10,12 or 15")
tip = int(input())
print("How many people to split the bit ?")
people = int(input())
bill_with_tip = tip/100 * bill + bill
print("Your bill with tip is",bill_with_tip)
bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person,2)
print("Each person should pay ",final_amount)
