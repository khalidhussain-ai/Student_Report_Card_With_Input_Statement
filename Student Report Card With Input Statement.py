
name = input("Enter student name: ")
English = int(input("Enter English marks: "))
Urdu = int(input("Enter Urdu marks: "))
Math = int(input("Enter Math marks: "))
Physics = int(input("Enter Physics marks: "))
Chemistry = int(input("Enter Chemistry marks: "))
Computer = int(input("Enter Computer marks: "))
Islamiat = int(input("Enter Islamiat marks: "))
Tarjamatulquran = int(input("Enter Tarjamatulquran marks: "))
total_marks = 545
obtain_marks = English + Urdu + Math + Physics + Chemistry + Computer + Islamiat + Tarjamatulquran
percentage = (obtain_marks / total_marks) * 100
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"
if percentage >= 50:
    status = "Pass"
else:
    status = "Fail"
print("\n----- Student Result -----")
print("Student Name    :", name)
print("Total Marks     :", total_marks)    
print("Obtained Marks  :", obtain_marks)
print("Percentage      :", round(percentage, 2), "%")
print("Grade           :", grade)

