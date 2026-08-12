a , b , c = map(int,input().split())
if a == b == c:
    print("equailateral")
elif a == b or b == c or c == a:
    print("isosceles")
else:
    print("scalene")