balance = int(input())
withdraw = int(input())
minimum_balance = int(input())
remaining = balance - withdraw
if remaining >= minimum_balance:
    print(f"withdraw sucessful","remaining balance is : ", {remaining})
else:
    print("insufficiant balance")

