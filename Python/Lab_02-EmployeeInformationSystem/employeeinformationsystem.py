name = input("Enter Employee Name: ")
print("  Data type:", type(name))

employee_id = int(input("Enter Employee ID: "))
print("  Data type:", type(employee_id))

salary = float(input("Enter Salary: "))
print("  Data type:", type(salary))

department = input("Enter Department: ")
print("  Data type:", type(department))

active = input("Is the employee active? (yes/no): ").strip().lower() == "yes"
print("  Data type:", type(active))

print()
print("--- Employee Details ---")
print(f"Name       : {name}")
print(f"ID         : {employee_id}")
print(f"Salary     : {salary}")
print(f"Department : {department}")
print(f"Active     : {active}")