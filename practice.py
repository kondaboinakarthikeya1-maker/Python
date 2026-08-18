n = int(input("Enter how many numbers : "))
first = int(input("Enter a number : "))
smallest = first
largest = first
for i in range(1,n):
    num = int(input("Enter a number : "))
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print(smallest)
print(largest)