"""
Q8. An extra day is added to the calendar almost every four years as
February 29, and the day is called a leap day. A leap year contains a leap
day
These are the conditions used to identify leap years:

1. if the year can be evenly divided by 4, it is then a leap year
2. but if the year is evenly divided by 4 and also by 100, then it is NOT a
leap year
3. but if the year is evenly divided by 4 and also by 400, then it is a leap
year

This means the years 2000 and 2400 are leap years, while 1800, 1900,
2100, 2200, 2300 and 2500 are NOT leap years.

Ask a year input from user. And tell if the year entered by user is leap or
not.
"""

"""
Normal year = 365 days.
Leap year = 366 days.
condition-1: year can be evenly divided by 4 means remainder is o.
year % 4 == 0 (leap year)

condition-2: year % 4 == 0 and year % 100 == 0 (Not a leap year).

condition-3: year % 4 == 0 and year % 400 == 0 (leap year).
"""
# Take year as input from the user
year: int = int(input("Enter a year: "))

# Check if the year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is NOT a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")
