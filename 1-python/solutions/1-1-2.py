# Code Challenge 1-1-2

bill = float(input("Enter the total bill amount: "))
tip = int(input("Enter the tip percentage: "))
tip_pct = tip / 100
diners = int(input("Enter the number of diners: "))

# Calculate the tip amount

total = bill + (bill * tip_pct)
share = total / diners

#OUTPUT
print("The total bill amount is: ", total)
print("Each diner should pay: ", share)
