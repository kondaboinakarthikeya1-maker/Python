recharge = float(input("Enter your recharge amount : "))
if recharge > 3000:
    discount = recharge * 0.15
elif 2000 <= recharge < 3000:
    discount = recharge * 0.10
elif 1000 <= recharge < 2000:
    discount = recharge * 0.5
elif 300 <= recharge < 1000:
    discount = recharge * 0.25
else:
    print("Enter valid Recharge ")
cashback = recharge - discount
print("Your Cash back is : ",discount)