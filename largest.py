n = int(input("enter numbers how many numbers : "))
largest = 0
for i in range(1,n+1):
    num = int(input("Enter a number : "))
    if num > largest:
        largest = num
print(largest)
