n = int(input("Enter a number : "))
# method 1
for i in range(0,n+1):
    if i % 3 == 0:
        print(i)



#method 2
for i in range(3,n+1,3):
    print(i)