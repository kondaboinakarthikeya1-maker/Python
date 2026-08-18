n = int(input("Enter a number : "))
if n % 3 == 0:
    start = n
else:
    start = n - (n % 3)
for i in range(start,0,-3):
    print(i)