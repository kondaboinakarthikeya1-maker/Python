n = int(input("Enter a number : "))
total = 0
while n > 0:
    n = n // 10
    total = total + 1
print(total)