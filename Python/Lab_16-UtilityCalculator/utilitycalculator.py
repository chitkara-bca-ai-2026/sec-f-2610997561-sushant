def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a multiplied by b."""
    return a * b


def divide(a, b):
    """Return a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """Return the remainder of a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    """Return base raised to exp. The default exponent is 2 (square)."""
    return base ** exp


def format_number(n):
    """Return an int if n has no decimal part, otherwise return the float."""
    if n == int(n):
        return int(n)
    return n

def is_valid_number(text):
    """Check if text is a number (optional minus sign, at most one dot)."""
    text = text.strip()
    if text.startswith("-"):
        text = text[1:]
    if text.count(".") == 1:
        text = text.replace(".", "")
    return text.isdigit()


def read_number(prompt, allow_empty=False):
    """Keep asking until the user enters a valid number.
    If allow_empty is True and the user presses Enter, return None."""
    while True:
        text = input(prompt).strip()
        if text == "" and allow_empty:
            return None
        if is_valid_number(text):
            return float(text)
        print("Invalid input. Please enter a valid number.")

OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
    "5": ("%", modulus),
}


def show_menu():
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: square)")
    print("7. View calculation history")
    print("8. Exit")


def save_result(history, a, symbol, b, result):
    """Build the record text, store it in history, and print it."""
    line = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}"
    history.append(line)
    print(f"[RESULT] {line}")


def show_history(history):
    if len(history) == 0:
        print("No calculations performed yet.")
        return
    print("\n--- Calculation History ---")
    for number, line in enumerate(history, start=1):
        print(f"{number}. {line}")

def main():
    history = []
    print("=== Modular Utility Calculator ===")

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("Exiting calculator. Goodbye!")
            break

        elif choice == "7":
            show_history(history)

        elif choice in OPERATIONS:
            symbol, func = OPERATIONS[choice]
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if symbol in ("/", "%") and b == 0:
                print("Error: cannot divide or take modulus by zero.")
            else:
                result = func(a, b)
                save_result(history, a, symbol, b, result)

        elif choice == "6":
            a = read_number("Enter base: ")
            b = read_number("Enter exponent (press Enter for default 2): ", allow_empty=True)
            if b is None:
                result = power(a)  
                b = 2                
            else:
                result = power(a, b)
            save_result(history, a, "^", b, result)

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()