import csv
import os

# Build the CSV path from this script's own folder, so it works no matter where you run it from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "students_data.csv")
THRESHOLD = 50   # Minimum marks to qualify


def print_header():
    # Column titles with fixed widths so the columns line up
    print(f"{'Roll_No':<10}{'Name':<15}{'Subject':<15}{'Marks':<6}")
    print("-" * 46)


def print_row(row):
    # row is a dictionary: keys are the column headers from the first line of the CSV
    print(f"{row['Roll_No']:<10}{row['Name']:<15}{row['Subject']:<15}{row['Marks']:<6}")


def read_all_students(filename):
    """Read the CSV file and display all student records."""
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)   # uses the first line as column names
            print("\n--- ALL STUDENTS ---")
            print_header()
            count = 0
            for row in reader:
                print_row(row)
                count += 1
            print("-" * 46)
            print(f"Total records: {count}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Keep it in the same folder as this script.")


def filter_students_above_threshold(filename, threshold=50):
    """Read the CSV file and display only students with marks above the threshold."""
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            print(f"\n--- STUDENTS WITH MARKS > {threshold} ---")
            print_header()
            count = 0
            for row in reader:
                # CSV values are text, so convert Marks to int before comparing
                if int(row["Marks"]) > threshold:
                    print_row(row)
                    count += 1
            print("-" * 46)
            print(f"Total qualified students: {count}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Keep it in the same folder as this script.")
    except ValueError:
        print("Error: Marks must be whole numbers in the CSV file.")


def main():
    print("=" * 40)
    print("   STUDENT RESULT ANALYSIS SYSTEM")
    print("=" * 40)

    while True:   # keep showing the menu until the user exits
        print("\nSelect an operation:")
        print("1. Display All Students from CSV")
        print("2. Filter Students (Marks > 50)")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            read_all_students(FILENAME)
        elif choice == "2":
            filter_students_above_threshold(FILENAME, THRESHOLD)
        elif choice == "3":
            print("Thank you for using Student Result Analysis System. Goodbye!")
            break   # exits the while loop and ends the program
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()