"""
Q7. Take Salary as input from User and Update the salary of an employee.
•
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, IO % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary: int = int(input("Enter user_salary: "))
increment = 0

if salary >= 50000:
    increment = 20
elif 20000 <= salary <= 50000:
    increment = 15
elif 10000 <= salary <= 20000:
    increment = 10
elif salary < 10000:
    increment = 5
else:
    increment = 0

# Calculate the incremented amount and the updated salary
increment_amount = (increment / 100) * salary
updated_salary = salary + increment_amount

# Print the results
print(f"Employee salary before increment is ₹{salary}.")
print(f"Increment applied: {increment}%.")
print(f"Increment amount: ₹{increment_amount:.2f}.")
print(f"Employee salary after increment is ₹{updated_salary:.2f}.")
