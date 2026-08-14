telugu = int(input("Enter your marks in Telugu  : "))
hindi = int(input("Enter your marks in Hindi : "))
english = int(input("Enter your marks in English : "))
maths = int(input("Enter your marks in Maths  : "))
science = int(input("Enter your marks in Science  : "))
social = int(input("Enter your marks in Social : "))
total = telugu+hindi+english+maths+science+social
percentage = total/6
if telugu < 35 or hindi < 35 or english < 35 or maths < 35 or science < 35 or social < 35:
    print("Your are failed")
elif 90 <= percentage < 100:
    result = "S grade"
elif 80 <= percentage < 90:
    result = "A grade"
elif 70 <= percentage < 80:
    result = "B grade"
elif 60 <= percentage < 70:
    presult = "C grade"
elif 50 <= percentage < 60:
    result = "D grade"
else:
    print("pass")
print("Your total marks are : ",total)
print("Your percentage is : ",percentage)
print("Your result is : ", result)
