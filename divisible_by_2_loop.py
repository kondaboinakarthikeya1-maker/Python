n = int(input("enter a value : "))
count = 0
for i in range(1,n+1):
    if i % 2 == 0 and i % 4 != 0:
        count += 1
print(count)