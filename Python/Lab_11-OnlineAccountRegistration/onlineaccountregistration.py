
username = input("Enter your username: ")
password = input("Enter your password: ")

length_pass = len(password) >= 8
length_msg = f"({len(password)} characters)"

has_digit = any(char.isdigit() for char in password)

has_uppercase = any(char.isupper() for char in password)

is_valid = length_pass and has_digit and has_uppercase

print("=========================================")
print("PASSWORD VALIDATION REPORT")
print("=========================================")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print()
print("--- Validation Rules ---")

print(f"[{'PASS' if length_pass else 'FAIL'}] Minimum 8 characters {length_msg}")
print(f"[{'PASS' if has_digit else 'FAIL'}] At least one digit")
print(f"[{'PASS' if has_uppercase else 'FAIL'}] At least one uppercase letter")
print()
print("--- Result ---")

if is_valid:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("=========================================")