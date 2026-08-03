age=int(input())
gender=input("Enter your gender (M/F) ") 
if age >= 21 and gender == "M":
    print("eligible for marriage")
elif age >= 18 and gender == "F":
    print("eligible for marriage")
else:
    print("not eligible for marriage")  