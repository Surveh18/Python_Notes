"""
Q6. Write a function that takes two integers (hours, minutes), converts
them to seconds, and adds them.

# Examples
• convert(l, 3) —> 3780
• convert(2, 0) —> 7200
• convert(O, O) —> O
Don't forget to return the result.
1 hr = 60 min
1 min = 60 sec
"""


def convert(hour: int, minutes: int) -> int:
    Total_seconds = (hour * 3600) + (minutes * 60)
    return Total_seconds


print(convert(1, 3))
print(convert(2, 0))
print(convert(0, 0))
