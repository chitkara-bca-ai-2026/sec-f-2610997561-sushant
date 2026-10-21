import sys

print("==================================================")
print("             SCHOOL RESULT PROCESSING             ")
print("==================================================")

student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")
print()

print("--- Enter Marks for 5 Subjects (0-100) ---")
marks = []
has_failed_subject = False

for i in range(1, 6):
    try:
        mark = float(input(f"Enter marks for Subject {i}: "))
    except ValueError:
        print("\nError: Invalid input. Marks must be a number.")
        sys.exit()
        
    if mark < 0 or mark > 100:
        print("\nError: Marks must be between 0 and 100. Exiting program.")
        sys.exit()
        
    if mark < 40:
        has_failed_subject = True
        
    marks.append(mark)
    
total_marks = sum(marks)
percentage = (total_marks / 500.0) * 100.0

if has_failed_subject:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

print("\n==================================================")
print("               STUDENT REPORT CARD               ")
print("==================================================")
print(f"  Student Name : {student_name}")
print(f"  Roll Number  : {roll_number}")
print("--------------------------------------------------")
print(f"  Total Marks  : {total_marks:.1f} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remark}")
print("==================================================")