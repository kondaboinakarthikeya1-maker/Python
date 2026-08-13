cgpa = float(input("enter your overall cgpa : "))
backlogs = int(input("enter no.of backlogs : "))
if cgpa >= 8.0 and backlogs == 0:
    print("eligible for placements")
else:
    print("not eligible for placements")