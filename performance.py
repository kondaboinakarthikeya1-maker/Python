score = float(input("Enter your performance score : "))
if 90 <= score <= 100:
    print("Excellent")
elif 75 <= score < 90:
    print("Good")
elif 65 <= score < 75:
    print("Average")
elif 50 <= score < 65:
    print("Need to improve")
else:
    print("Poor Performance")