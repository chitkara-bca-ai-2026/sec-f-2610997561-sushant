import os

FILENAME = "student_marks.txt"


def create_sample_file(filename):
    """Create the file with sample records if it does not exist yet."""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("Aman,85\n")
            f.write("Riya,92\n")
            f.write("Karan,78\n")


def store_student(filename, name, marks):
    """Append one record in the format name,marks."""
    with open(filename, "a") as f:   
        f.write(f"{name},{marks}\n")
    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")


def display_and_calculate_average(filename):
    """Show all records in a table and print the class average."""
    if not os.path.exists(filename):
        print("[ERROR] File not found. No records to display.")
        return

    names = []
    marks_list = []
    with open(filename, "r") as f:
        for line in f:                 
            line = line.strip()          
            if line == "":
                continue
            name, marks = line.split(",")
            names.append(name.strip())
            marks_list.append(int(marks)) 

    if len(marks_list) == 0:
        print("[INFO] No records found.")
        return

    total = sum(marks_list)
    average = total / len(marks_list)

    print("\n" + "=" * 45)
    print("STUDENT MARKS LEDGER".center(45))
    print("=" * 45)
    print(f"{'No.':<6}{'Student Name':<20}{'Marks Obtained':<15}")
    print("-" * 45)
    for i in range(len(names)):
        print(f"{i + 1:<6}{names[i]:<20}{marks_list[i]:<15}")
    print("-" * 45)
    print(f"Total Students : {len(marks_list)}")
    print(f"Total Marks    : {total}")
    print(f"Class Average  : {average:.2f}")
    print("=" * 45)


def add_student_marks():
    """Ask for name and marks, validate, then store the record."""
    name = input("Enter Student Name: ").strip()
    while True:
        try:
            marks = int(input("Enter Marks (0-100): "))
        except ValueError:
            print("[ERROR] Please enter a whole number.")
            continue
        if 0 <= marks <= 100:
            break
        print("[ERROR] Marks must be between 0 and 100.")
    store_student(FILENAME, name, marks)


def main():
    create_sample_file(FILENAME)
    print("=" * 45)
    print("STUDENT MARKS FILE HANDLING TOOL".center(45))
    print("=" * 45)

    while True:
        print("\nSelect an operation:")
        print("1. Add & Store Student Marks")
        print("2. Display Records & Class Average")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            add_student_marks()
        elif choice == "2":
            display_and_calculate_average(FILENAME)
        elif choice == "3":
            print("Thank you for using Student Marks Tool. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()