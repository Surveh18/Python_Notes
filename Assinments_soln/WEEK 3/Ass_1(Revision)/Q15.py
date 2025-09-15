"""
Q15. Create a function that takes three values:
• h hours
• m minutes
• s seconds
Return the value that's the longest duration.
Examples:
• longest_time(l, 59, 3598) -> 1
• longest_time(2, 300, 15000) -> 300
• longest_time(l5, 955, 59400) -> 59400

No two durations will be the same.
"""


def longets_time(h, m, s):
    hours_in_sec = h * 3600
    min_in_sec = m * 60
    sec_in_sec = s * 1
    if hours_in_sec > min_in_sec and hours_in_sec > sec_in_sec:
        return h
    elif min_in_sec > hours_in_sec and min_in_sec > sec_in_sec:
        return m
    elif sec_in_sec > hours_in_sec and sec_in_sec > min_in_sec:
        return s


print(longets_time(1, 59, 3598))
print(longets_time(2, 300, 15000))
print(longets_time(15, 955, 59400))
