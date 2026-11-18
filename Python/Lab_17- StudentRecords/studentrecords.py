def calculate_results(marks):
    """Receives a list of marks and returns (total, average)."""
    total = sum(marks)
    average = total / len(marks)
    return total, average


def display_student(roll_no, student):
    """Receives roll number and student dictionary, then prints one formatted line."""
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll_no} | Name: {student['Name']} | "
          f"Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}")


def add_student(records, roll, name, marks):
    """Adds a new student unless the roll number already exists."""
    if roll in records:
        print(f"Error: Roll Number {roll} already exists.")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print(f"Student '{name}' (Roll No: {roll}) added successfully.")


def main():
    students = {
        "101": {"Name": "Aman", "Marks": [85, 90, 78]},
        "102": {"Name": "Riya", "Marks": [92, 88, 95]},
        "103": {"Name": "Karan", "Marks": [70, 80, 75]},
    }

    print("=" * 40)
    print("   STUDENT RECORDS MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        print("\nSelect an option:")
        print("1. Display All Students")
        print("2. Add New Student")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            print("\n-- All Student Records --")
            for roll, student in students.items():
                display_student(roll, student)
            print(f"Total Students: {len(students)}")

        elif choice == "2":
            print("\n-- Add New Student --")
            roll = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            marks = []
            for i in range(1, 4):
                marks.append(int(input(f"Enter marks for Subject {i}: ")))
            add_student(students, roll, name, marks)

        elif choice == "3":
            roll = input("Enter Roll Number to search: ")
            student = students.get(roll)
            if student:
                display_student(roll, student)
            else:
                print(f"No student found with Roll Number {roll}.")

        elif choice == "4":
            print("Thank you for using the Student Records System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()