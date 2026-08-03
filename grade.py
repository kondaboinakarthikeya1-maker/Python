n = int(input("enter your marks : "))
if n > 100:
    print("enter marks less than 100")
elif 90 <= n < 100:
    print("Grade A")
elif 75 <= n < 90:
    print("Grade B")
elif 65 <= n < 75:
    print("Grade c")
elif 50 <= n < 65:
    print("Grade D")
elif n < 50:
    print("Fail")