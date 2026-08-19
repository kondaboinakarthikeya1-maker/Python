n = int(input("Enter a number : "))
if n % 2 == 0:
    start = n
else:
    start = n-1
for i in range(start,0,-2):
    print(i)