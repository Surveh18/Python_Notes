"""
QIO. Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.

# Example 1
printPattern(5)

# Output
-5 -4 -3 -2 -1 0 1 2 3 4 5

# Example 2
printPattern(-9)

# Output
-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
"""

# Read the number from the user
i = int(input("Enter the number: "))


# Determine the starting and ending points
def printPattern(i):
    if i < 0:
        start_up = i
        end_up = abs(i)
    else:
        start_up = 0
        end_up = i

    # Loop to print the sequence from start to end
    while start_up <= end_up:
        print(start_up, end=" ")
        start_up += 1


# Call the function with the user input
printPattern(i)
