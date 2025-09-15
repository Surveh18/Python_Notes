"""
Q7.Keep asking numbers from user until the user enters 0. Then display
the average of all numbers.
"""


def avg():
    count: int = 0
    total: int = 0
    while True:
        n = int(input("Enter a number (enter 0 to finish): "))
        if n == 0:
            break
        total += n
        count += 1
    print(f"The avg of all numbers is {total/count}")


avg()
