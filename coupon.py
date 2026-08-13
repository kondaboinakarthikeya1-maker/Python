amount = float(input("Enter your amount : "))
coupon = input("Enter coupon code : ")
if amount >= 1500 and coupon == "save10":
    discount = amount * 0.10
    print("coupon applied")
    print("discount ",discount)
    print("amount should be payble ",amount - discount)
else:
    print("coupon not valid")