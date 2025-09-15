"""
Q4. Write a Python program that takes four numbers from the user.
Implement a function to find the average of the first three numbers. Then,
create another function to check if the average is greater than or equal to
the fourth number. Make sure to use these two functions to determine and
print whether the average is greater than or equal to the fourth number or
not.

Enter the first number:  1
Enter the second number: 54
Enter the third number:  23
Enter the fourth number: 47

# Output
The average of 1, 54, and 23 is: 26.0
The average is less than 47.

"""

# Taking four numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))


# Function to calculate the average of the first three numbers
def calculate_avg(num1: float, num2: float, num3: float) -> float:
    return (num1 + num2 + num3) / 3


# Function to check if the average is greater than or equal to the fourth number
def check_avg_vs_fourth(average: float, num4: float) -> bool:
    return average >= num4


# Calculate the average of the first three numbers
average = calculate_avg(num1, num2, num3)

# Print the average
print(f"The average of {num1}, {num2}, and {num3} is: {average}")

# Check if the average is greater than or equal to the fourth number and print the result
if check_avg_vs_fourth(average, num4):
    print(f"The average is greater than or equal to {num4}.")
else:
    print(f"The average is less than {num4}.")
