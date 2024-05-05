# day two of learning python, today we are creating a tip calcuator by taking the inputs like total bill, tip percentage and number of people to split the bill between 

print("wellcome to the tip calculator")
totalBill = input("what wat the total bill? \n $")
tip = input("what is the pecentag of tip you want to give\n 10 12 15 ?\n")
people = input("how many people to split the bill?\n")

totalBill = float(totalBill)
people=int(people)
tip=int(tip)
shouldPay=(totalBill)*(1+tip/100)
shouldPay=shouldPay/people
totalAmt=round(shouldPay,2)
print(f"each person should pay {totalAmt}")
