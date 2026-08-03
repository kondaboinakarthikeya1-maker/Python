n = int(input("Enter the number"))
if 0 <= n >= 12:
    print("invalid input")
elif 1 <= n <= 3:
    print("Q1")
elif 4 <= n <= 6:
    print("Q2")
elif 7 <= n <= 9:
    print("Q3")
else:
    print("Q4")