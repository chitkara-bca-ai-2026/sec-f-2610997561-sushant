import os

FILENAME = "report.txt"

SAMPLE_TEXT = """Annual Technology and AI Progress Report.
The adoption of Artificial Intelligence accelerated across business units.
AI algorithms improved diagnostic accuracy in healthcare operations.
Data engineering pipelines were upgraded to support real-time data streaming.
The company plans further investments in AI research and machine learning.
"""


def create_sample_file(filename):
    """Create report.txt with sample text if it does not already exist."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(SAMPLE_TEXT)
        print(f"Sample file '{filename}' created.")


def search_keyword(filename, keyword):
    """Search for a keyword (case-insensitive) and show matching lines."""
    keyword_lower = keyword.lower()
    total_occurrences = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"--- Search Results for '{keyword}' ---")
            for line_number, line in enumerate(file, start=1):
                line_lower = line.lower()
                if keyword_lower in line_lower:
                    count = line_lower.count(keyword_lower)
                    total_occurrences += count
                    label = "match" if count == 1 else "matches"
                    print(f"Line {line_number} ({count} {label}): {line.strip()}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return

    if total_occurrences == 0:
        print(f"'{keyword}' was not found in the document.")
    else:
        print(f"\n[FOUND] Total occurrences of '{keyword}': {total_occurrences}")


def display_document(filename):
    """Read and display every line of the document with line numbers."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"--- Full Report Document ({filename}) ---")
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:>2} | {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")


def main():
    create_sample_file(FILENAME)

    print("=" * 50)
    print("KEYWORD SEARCH UTILITY".center(50))
    print("=" * 50)

    while True:
        print("\nSelect an operation:")
        print("1. Search Keyword in Document")
        print("2. View Full Document")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            keyword = input("Enter keyword to search: ").strip()
            if keyword == "":
                print("Keyword cannot be empty.")
            else:
                search_keyword(FILENAME, keyword)
        elif choice == "2":
            display_document(FILENAME)
        elif choice == "3":
            print("Thank you for using Keyword Search Utility. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()