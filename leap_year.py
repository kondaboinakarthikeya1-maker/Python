year=int(input())
if year % 100 == 0 and year % 400 == 0:
    print("not a leap year")
elif year % 4 == 0 :
    print("leap year")
else:
    print("not a leap year")