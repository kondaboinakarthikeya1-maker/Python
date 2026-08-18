n = int(input("Enter how many numbers : "))
count = 0
total = 0
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        count = count + 1
        total = total + i
        print(i)
print("Count : ",count)
print("Total : ",total)