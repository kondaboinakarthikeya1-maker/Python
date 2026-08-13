age = int(input("Enter your age : "))
if age < 13 :
    print("eligible for UNRESTRICTED movies ")
elif 13 <= age < 18:
    print("eligible for U/A movies ")
elif age >= 18:
    print("eligible for Adult movie ")

