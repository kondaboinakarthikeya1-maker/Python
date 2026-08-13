salary = int(input("Enter your monthly salary : "))
age = int(input("Enter your age : "))
credit_score = int(input("Enter your credit score : "))
if salary >= 50000 and age >= 21 and credit_score > 750:
    print("eligible for loan")
else:
    print("not eligible")