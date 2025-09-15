"""
Q1 – Maximum value
fruits = {"apple": 100, "banana": 40, "mango": 60}

Task: Find the fruit with maximum quantity.

Tumhe sochna hai kaise values compare karoge aur kaunse key return karoge.
"""

fruits = {"apple": 100, "banana": 40, "mango": 60}
max_val = int()
max_fruit = ""

for fruit, qty in fruits.items():
    if qty > max_val:
        max_val = qty
        max_fruit = fruit
print(f"Fruit with max qty = {dict([(max_fruit, max_val)])}")
# Fruit with max qty = {'apple': 100}
