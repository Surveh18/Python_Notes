"""
Q5. A farmer is asking you to tell him how many legs can be counted among
all his animals. The farmer breeds three species:

• chickens = 2 legs
• cows = 4 legs
• pigs = 4 legs

The farmer has counted his animals and he gives you a subtotal for each
species. You have to implement a function that returns the total number of
legs of all the animals.

# Examples:
• animals(2, 3, 5) - 36
• animals(l, 2, 3) - 22
• animals(5, 2, 8) - 50

Don't forget to return the result.
The order of animals passed is animals(chickens, cows, pigs).
"""


def animals(chickens: int, cows: int, pigs: int) -> int:
    total_count = (chickens * 2) + (cows * 4) + (pigs * 4)
    return total_count


print(animals(2, 3, 5))
print(animals(1, 2, 3))
print(animals(5, 2, 8))
