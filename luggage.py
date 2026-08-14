weight = float(input("Enter your luggage Weight in kg : "))
allowed = 20
if weight <= allowed:
    print("Luggage is accepted , no extra charge")
elif weight > allowed:
    extra = weight - allowed
    charge = extra * 200
    print("Extra luggage is",extra,"kg")
    print("Your charge for Extra luggage is : ",charge)
    
