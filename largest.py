n = int(input("enter numbers how many numbers : "))
largest = int(input())
for i in range(n):
    num = int(input("Enter a number : "))
    if num < largest:
        largest = num
print(largest)
