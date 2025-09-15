"""
Take values of length and breadth of a rectangle from user and check if it is square or not.
"""

Length: float = float(input("Enter the length of the rectangle: "))
breadth: float = float(input("Enter the breadth of the rectangle: "))

if Length == breadth:
    print(
        f"length = {Length} and breadth = {breadth} is equal so the rectangle is square."
    )
else:
    print(
        f"Length = {Length} and breadth = {breadth} is NOT equal so the rectangle is NOT a square."
    )
"""
Sample input:
1.length = 5 breadth = 5  
2.length = 6 breadth = 4  


Output:
1.length = 5 and breadth = 5 is equal so the rectangle is square.
2.length = 6 breadth = 4 is NOT equal so the rectangle is NOT a square.
"""
