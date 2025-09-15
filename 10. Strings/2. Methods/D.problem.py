"""
Example 1 :
a = 12
b = 10
o/p = 22

Example 2 :
a = "abc"
b = "xyz"
o/p = abcxyz

Example 3 :
a = 12
b = "abc"
o/p = 12abc
"""

a = input("Enter something: ")
b = input("Enter something: ")

if a.isdigit() and b.isdigit():
    print(int(a) + int(b))
else:
    print(a + b)
