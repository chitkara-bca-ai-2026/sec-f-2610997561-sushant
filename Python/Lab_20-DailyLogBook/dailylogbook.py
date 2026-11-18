import os

FILENAME = "daily_log.txt"

SAMPLE_ENTRIES = [
    "09:00 AM - System server startup verified.",
    "10:30 AM - Morning attendance synchronized.",
    "02:15 PM - Network security patch applied.",
]


def create_sample_file_if_missing(filename):
    """Pre-populate the log file with sample entries, but only if it does not exist yet."""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            for entry in SAMPLE_ENTRIES:
                f.write(entry + "\n")


def append_entry(filename, entry):
    """Add one new entry at the end of the file without erasing old entries."""
    with open(filename, "a") as f:
        f.write(entry + "\n")  
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    """Read the whole file and show every entry with a number."""
    with open(filename, "r") as f: 
        lines = [line.strip() for line in f if line.strip()]

    print("\n" + "=" * 15 + " DAILY LOG BOOK " + "=" * 15)
    for number, line in enumerate(lines, start=1):
        print(f"[{number:02d}] {line}")
    print(f"\nTotal Logged Entries: {len(lines)}")
    print("=" * 46)


def main():
    create_sample_file_if_missing(FILENAME)
    print("=" * 12 + " OFFICE DAILY LOG BOOK " + "=" * 12)

    while True: 
        print("\nSelect an operation:")
        print("1. Add Log Entry")
        print("2. Display Complete Log")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            entry = input("Enter log entry: ").strip()
            if entry:
                append_entry(FILENAME, entry)
            else:
                print("[ERROR] Empty entry was not saved.")

        elif choice == "2":
            display_log(FILENAME)

        elif choice == "3":
            print("Thank you for using the Daily Log Book. Goodbye!")
            break 

        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()