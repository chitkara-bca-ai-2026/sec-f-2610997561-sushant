
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

while True:
    print("\n================================================")
    print("      STUDENT INFORMATION MANAGEMENT SYSTEM     ")
    print("================================================")
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print("------------------------------------------------")
    
    choice = input("Enter your choice (1-7): ").strip()
    print() 

    if choice == "1":
        print("--- Enrolled Student Records ---")
        if not students:
            print("No student records available.")
        else:
            for roll_no, info in students.items():
                print(f"Roll No: {roll_no}  | Name: {info['Name']:<9} | Branch: {info['Branch']}")
                print(f" | Sem: {info['Semester']} | Marks: {info['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        
        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print(f"\n[ERROR] Record for Roll No {roll} not found.")

    elif choice == "3":
        print("--- Register New Student ---")
        roll = input("Enter Roll Number: ").strip()
        
        if roll in students:
            print(f"\n[ERROR] Student with Roll Number {roll} already exists!")
        else:
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch (e.g. BCA AI): ").strip()
            semester = input("Enter Semester: ").strip()
            
            print("Enter marks obtained in 3 subjects:")
            try:
                sub1 = int(input("  Subject 1: "))
                sub2 = int(input("  Subject 2: "))
                sub3 = int(input("  Subject 3: "))
                
                students[roll] = {
                    "Name": name,
                    "Branch": branch,
                    "Semester": semester,
                    "Marks": [sub1, sub2, sub3]
                }
                print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
            except ValueError:
                print("\n[ERROR] Invalid numerical input for marks. Registration canceled.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ").strip()
        student = students.get(roll)
        
        if not student:
            print(f"[ERROR] Student with Roll Number {roll} not found.")
        else:
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            field_choice = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()
            
            if field_choice == "1":
                new_branch = input("Enter new branch: ").strip()
                student["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field_choice == "2":
                new_sem = input("Enter new semester: ").strip()
                student["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid choice. Update aborted.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ").strip()
        student = students.get(roll)
        
        if not student:
            print(f"[ERROR] Student with Roll Number {roll} not found.")
        else:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            
            result_status = "PASS" if average >= 40 else "FAIL"
            
            print("\n============ ACADEMIC REPORT ============")
            print(f"Student Name : {student['Name']} (Roll No: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {result_status}")
            print("=========================================")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ").strip()
    
        removed_student = students.pop(roll, None)
        
        if removed_student:
            print(f"[SUCCESS] Record for '{removed_student['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"[ERROR] Record for Roll No {roll} not found.")

    elif choice == "7":
        print("Thank you for using Student Information Management System.")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid selection! Please enter a number between 1 and 7.")