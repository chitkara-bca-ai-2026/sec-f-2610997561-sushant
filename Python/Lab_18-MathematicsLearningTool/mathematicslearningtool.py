def factorial(n):
    """Return n! using recursion."""

    if n <= 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed) using recursion."""

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def read_non_negative_int(prompt):
    """Keep asking until the user types a whole number that is 0 or greater."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("[ERROR] Please enter a whole number.")
            continue

        if value < 0:
            print("[ERROR] Number must be 0 or greater.")
            continue

        return value


def print_menu():
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")


def main():
    print("=" * 40)
    print("      MATHEMATICS LEARNING TOOL")
    print("=" * 40)

    while True:
        print_menu()
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            n = read_non_negative_int("Enter a non-negative integer: ")
            print(f"[RESULT] Factorial of {n} ({n}!) = {factorial(n)}")

        elif choice == "2":
            terms = read_non_negative_int("Enter number of terms to generate: ")
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

        elif choice == "3":
            print("Thank you for using the Mathematics Learning Tool. Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()