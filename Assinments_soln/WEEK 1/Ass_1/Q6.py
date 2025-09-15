"""
Q6. Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win = 4 points, 1 tie = 2 points)
"""

games_played: int = int(input("Enter numbr of games_played: "))
games_won: int = int(input("Enter numbr of games_won: "))
games_loss: int = int(input("Enter numbr of games_loss: "))

# Calculate the number of ties.
games_tie = games_played - games_won - games_loss
print(f"games_tie = {games_tie}")

# Calculate total points.
total_points = (games_won * 4) + (games_tie * 2)
print(f"Total points are {total_points}")

"""
Sample input:
games_played = 20
games_won = 10
games_loss = 5

Output:
games_tie = 5
Total points are 50
"""
