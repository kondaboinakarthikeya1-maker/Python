n = int(input())
if n > 100:
    print("invalid marks , enter below 100")
elif 90 <= n <= 100:
    print("grade A")
elif 75 <= n < 90:
    print("grade B")
elif 60 <= n < 75:
    print("grade C")
elif 50 <= n < 60:
    print("grade D")
elif n <= 35:
    print("Better luck next time")

