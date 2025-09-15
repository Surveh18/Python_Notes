"""
Q4. Create a function that takes the number of wins, draws and losses and
calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 points
loss get 0 points

# Examples:
• football_points(3, 4, 2) -> 13
• football_points(5, O, 2) -> 15
• football_points(O, O, 1) ->  0

Inputs will be numbers greater than or equal to O.
"""


def football_points(wins: int, draws: int, loss: int) -> int:
    total_points = (wins * 3) + (draws * 1) + (loss * 0)
    return total_points


print(football_points(3, 4, 2))
print(football_points(5, 0, 2))
print(football_points(0, 0, 1))
