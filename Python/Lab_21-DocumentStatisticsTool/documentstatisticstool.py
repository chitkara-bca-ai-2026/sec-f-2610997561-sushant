import os

FILENAME = "document.txt"

SAMPLE_TEXT = """Artificial Intelligence is transforming modern industries.
Python provides powerful libraries for text processing and data analysis.
Developers use file handling to store and retrieve persistent records.
Modular programming ensures code is clean, reusable, and easy to maintain.
"""


def create_sample_file(filename):
    """Create the file with sample text if it does not exist yet."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(SAMPLE_TEXT)
        print(f"Sample file '{filename}' created.")


def get_document_statistics(filename):
    """Return a tuple: (line_count, word_count, char_count)."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        word_count += len(line.split())
        char_count += len(line)

    return line_count, word_count, char_count


def display_document(filename):
    """Print each line of the file with its line number."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"--- Document Preview ({filename}) ---")
    for number, line in enumerate(lines, start=1):
        print(f"{number:>3} | {line.rstrip()}")


def file_is_ready(filename):
    """Defensive check: make sure the file exists before processing it."""
    if not os.path.exists(filename):
        print(f"Error: '{filename}' not found in this folder.")
        return False
    return True


def print_menu():
    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")


def main():
    print("=" * 45)
    print("        DOCUMENT STATISTICS ANALYZER")
    print("=" * 45)

    create_sample_file(FILENAME)

    while True:
        print_menu()
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            if not file_is_ready(FILENAME):
                continue
            line_count, word_count, char_count = get_document_statistics(FILENAME)
            print("\n" + "=" * 16 + " DOCUMENT REPORT " + "=" * 16)
            print(f"Target File      : {FILENAME}")
            print(f"Total Lines      : {line_count}")
            print(f"Total Words      : {word_count}")
            print(f"Total Characters : {char_count}")
            print("=" * 42)

        elif choice == "2":
            if not file_is_ready(FILENAME):
                continue
            display_document(FILENAME)

        elif choice == "3":
            print("\nThank you for using Document Statistics Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()