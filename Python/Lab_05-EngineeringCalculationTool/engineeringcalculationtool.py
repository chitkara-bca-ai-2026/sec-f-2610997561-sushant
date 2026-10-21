import math

print("========================================")
print("      ENGINEERING CALCULATION TOOL      ")
print("========================================")

val = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))

dec_val = float(input("Enter a decimal measurement: "))

power = math.pow(val, exp)
sqrt_val = math.sqrt(val)
ceil_val = math.ceil(dec_val)
floor_val = math.floor(dec_val)

print("\n--- Results ---")
print(f"{'Value':<20} : {val}")
print(f"{'Exponent':<20} : {exp}")
print(f"{'Power (pow)':<20} : {power}")
print(f"{'Square Root (sqrt)':<20} : {sqrt_val:.4f}")
print(f"{'Decimal Value':<20} : {dec_val}")
print(f"{'Ceil Value':<20} : {ceil_val}")
print(f"{'Floor Value':<20} : {floor_val}")
print("========================================")