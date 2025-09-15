"""
Q1. Write a function that converts hours into seconds.
# Examples:
how_many_seconds(2) -> 7200
how_many_seconds(10) -> 36000
how_many_seconds(24) -> 86400

seconds = hours x 3600
# Explanation
-> 1 hour = 60 min
-> 1 min = 60 sec
-> 1 Hour consist of 60 min & 60 sec
-> Therefore 1 Hour is equal to 60 x 60 = 3600
"""


def how_many_seconds(num: int) -> int:
    return num * 3600


print(how_many_seconds(2))
print(how_many_seconds(10))
print(how_many_seconds(24))
