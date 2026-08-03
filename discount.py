amount = float(input("Enter your bill : "))
if amount >= 5000:
    discount = amount * 0.20
elif 3000 <= amount < 5000:
    discount = amount * 0.15
elif 2000 <= amount < 3000:
    discount = amount * 0.10
else:
    discount = 0
bill = amount - discount
print("Discount",discount)
print("Amount to pay : ",bill)