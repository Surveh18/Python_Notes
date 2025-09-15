"""
Q4. Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7)
using function.
"""

# Question 7 will be solved here.

salary: int = int(input("Enter user_salary: "))


def employee_salary(salary: int) -> None:
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
