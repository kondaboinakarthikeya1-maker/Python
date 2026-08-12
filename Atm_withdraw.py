print("********ATM********")
balance = float(input("Enter balance : "))
withdraw = float(input("Enter withcdraw amount : " ))
if withdraw <= 0:
    print("Invalid withdrawal")
elif withdraw >= balance:
    print("Insufficiant balance")
else:
    print("With draw Sucessful")
    print("remaining balance : ",balance - withdraw)
