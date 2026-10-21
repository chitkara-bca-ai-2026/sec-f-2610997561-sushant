
print("====================================")
print("    CALENDAR VERIFICATION SYSTEM    ")
print("====================================")

try:
    year = int(input("Enter year: "))
except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

if year <= 0:
    print("Error: Year must be a positive integer greater than 0.")
    exit()

print("------------------------------------")

status = ""
days_in_year = 0
days_in_february = 0
reason = ""

if year % 100 == 0:
    if year % 400 == 0:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_february = 29
        reason = "Century year divisible by 400"
    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_february = 28
        reason = "Century year not divisible by 400"
else:
    if year % 4 == 0:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_february = 29
        reason = "Divisible by 4 and not a century year"
    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_february = 28
        reason = "Not divisible by 4"

print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {days_in_year} days")
print(f"Days in February: {days_in_february} days")
print(f"Reason: {reason}")
print("------------------------------------")