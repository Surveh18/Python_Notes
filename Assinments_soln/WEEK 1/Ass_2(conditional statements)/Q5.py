"""
Q5. Write a program to calculate bill. Ask the final amount from the user
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 -10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
"""

# Input the final amount
final_amount: float = float(input("Enter the final amount: "))

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
