age = int(input("Enter your Age : "))
health = input("Enter your Health condition (Good/poor): ")
if age <= 30 and health == "good":
    premium = "2500"
if age <= 30 and health == "poor":
    premium = "5000"
elif 30 < age < 50 and health == "good":
    premium = "10000"
elif 30 < age < 50 and health == "poor":
    premium = "15000"
elif age > 50 and health == "good":
    premium = "20000"
elif age > 50 and health == "poor":
    premium = "25000"
else:
    premium = "30000"
print("Your premium is : ",premium)