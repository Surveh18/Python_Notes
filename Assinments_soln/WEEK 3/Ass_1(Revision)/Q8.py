"""
Q8. Create a function that takes two arguments: the original price and the
discount percentage as integers and returns the final price after the
discount.

# Examples:
• dis(1500, 50) —> 750
• dis(89, 20) —> 71.2
• dis(100, 75) —> 25

Your answer should be rounded to two decimal places.
"""


def dis(original_price: float, discount_percentage: float) -> float:
    final_price = original_price - (original_price * (discount_percentage / 100))
    return round(final_price, 2)


print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))
