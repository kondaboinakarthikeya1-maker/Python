n=int(input())
if n >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting ,you have to wait upto", 18-n,"years")