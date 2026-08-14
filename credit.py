balance = float(input("Enter your balance : "))
limit = float(input("Enter your daily limit : "))
amount = float(input("enter your Transaction amount : "))
if amount <= balance and amount <= limit:
    print("Transaction Aproved")
else:
    print("Transcation Failed")