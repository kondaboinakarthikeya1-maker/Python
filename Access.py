role = input("enter your role : ")
if role == "admin":
    print("full access granted")
elif role == "manager":
    print("manager access granted")
elif role == "employee":
    print("employee acess granted")
else:
    print("acess denied")