"""
Take user_input start(s) and end(e).
print how many even numbers are there between start(s) and end(e).
"""


def countEven(s, e):
    i = s
    count = 0
    while i <= e:
        if i % 2 == 0:
            count = count + 1  # increase count by 1 if i is even.
        i += 1  # move to the nxt number.
    return count


print(countEven(s=1, e=22))
print(f"Number of even numbers = {countEven(1,22)}")
# Upperline can be also wriiten Alternatively.
