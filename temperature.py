n = float(input("enter the temperature in Celsius: "))
if n > 100:
    print("temperature is hot")
elif n < 0:
    print("temperature is cold")
else:
    print("temperature is moderate")