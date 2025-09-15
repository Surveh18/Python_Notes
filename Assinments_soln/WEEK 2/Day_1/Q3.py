"""
Q3. Attempt the same bill calculator question (Week 1 - Assignment 2 -
Q5) but using function. Try calling function with different bill amount as a
parameter and check the output.
"""

final_amount: float = float(input("Enter the final amount: "))


def bill_calc(final_amount: int) -> None:
    # Initialize discount and discounted amount
    discount: float = 0


# Determine the discount percentage based on the amount
if final_amount > 50000:
    discount = 30
elif 40000 <= final_amount <= 49999:
    discount = 25
elif 30000 <= final_amount <= 39999:
    discount = 20
elif 10000 <= final_amount <= 29999:
    discount = 10
else:
    discount = 0

# Calculate the discount amount
discount_amount = (discount / 100) * final_amount

# Calculate the final amount to be paid after discount
amount_to_pay = final_amount - discount_amount

# Print the results
print(f"Original Amount: ₹{final_amount:.2f}")
print(f"Discount Applied: {discount}%")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Amount to be Paid: ₹{amount_to_pay:.2f}")
