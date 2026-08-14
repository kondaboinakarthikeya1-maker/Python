severity = int(input("Enter severity level from (1 - 5) : "))
if severity == 5:
    print("Critical - Immediate treatment required")
elif severity == 4:
    print("Severe - Urgent treatment required")
elif severity == 3:
    print("Moderate - Treatment required soon")
elif severity == 2:
    print("Mild - Can wait")
elif severity == 1:
    print("Very mild - Low priority")
else:
    print("Please enter valid severity level")
    