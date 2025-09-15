"""
Q16. Create a function which takes two strings (pl and p2 — which
represent player 1 and 2) as arguments and returns a string stating the
winner in a game of Rock, Paper, Scissors.

Each argument will contain a single string: "Rock", "Paper", or "Scissors".
Return the winner according to the following rules:

• Rock beats Scissors
• Scissors beats Paper
• Paper beats Rock

If pl wins, return the string "The winner is pl"- If p2 wins, return the string
"The winner is p2" and if pl and p2 are the same, return "It's a draw".

Examples:
• rps("Rock", "Paper") "The winner is p2"
• rps("Scissors", "Paper") "The winner is p1"
• rps("Paper", "Paper") "It's a draw"
"""


def rps(p1, p2):
    if p1 == p2:
        return "It's a draw"
    elif p1 == "Rock" and p2 == "Scissors":
        return "The winner is p1"
    elif p1 == "Scissors" and p2 == "Paper":
        return "The winner is p1"
    elif p1 == "Paper" and p2 == "Rock":
        return "The winner is p1"
    else:
        return "The winner is p2"


print(rps("Rock", "Paper"))
print(rps("Scissors", "Paper"))
print(rps("Paper", "Rock"))
