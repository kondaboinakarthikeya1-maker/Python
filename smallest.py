n = int(input("Enter how many numbers : "))
smallest = n
for i in range(1,n + 1):
    num = int(input("Enter a number : "))
    if num < smallest:
        smallest = num
print(smallest) 