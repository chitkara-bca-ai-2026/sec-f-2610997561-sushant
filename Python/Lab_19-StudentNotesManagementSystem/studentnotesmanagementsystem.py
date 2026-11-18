import os

NOTES_FILE = "notes.txt"


def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    if not os.path.exists(filename):
        return "No notes file exists yet. Please write some notes first."

    with open(filename, "r") as file:
        return file.read()


def display_menu():
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")


def main():
    print("=" * 40)
    print("     STUDENT NOTES MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        display_menu()
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            content = input("Enter notes to save: ")
            write_notes(NOTES_FILE, content)

        elif choice == "2":
            print(f"\n--- Notes Content ({NOTES_FILE}) ---")
            print(read_notes(NOTES_FILE))

        elif choice == "3":
            print("\nThank you for using the Notes Management System. Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()