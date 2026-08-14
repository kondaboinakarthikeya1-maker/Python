stock = int(input("Enter available stock : "))
payment = input("Enter your payment status (paid/not paid) : ")
location = input("Enter delivery location (Available/not Available) : ")
if stock > 0 and payment == "paid" and location == "available":
    print("Oreder Confirmed")
    stock -= 1
    print("Remaing Stock is : ",stock)
elif stock < 0:
    print("order not confirmed")
    print("Reason : Out of stock")
elif payment != "paid":
    print("order not confirmed")
    print("Reason : payment not done")
elif location != "available":
    print("order not confirmed")
    print("Reason : Delivery not available in this location")
