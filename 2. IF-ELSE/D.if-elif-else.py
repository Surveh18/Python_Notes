"""
ELIF- condition

marks = 91

91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
60 down -> FAIL

"""

# ELIF condition can be use in program as many as we want.

# Type 1
# marks = 112
# if marks >= 91 and marks <= 100:
#     print("A")
# elif marks >= 81 and marks <= 90:
#     print("B")
# elif marks >= 71 and marks <= 80:
#     print("C")
# elif marks >= 61 and marks <= 70:
#     print("D")
# elif marks >= 0 and marks <= 60:
#     print("FAIL")
# else:
#     print("Invalid input")
# output(Type -1)-Invalid input


# Type - 2
mks = 95
# When we write multiple elif
if mks >= 91 and mks <= 100:
    print("A")
if mks >= 81 and mks <= 90:
    print("B")
if mks >= 71 and mks <= 80:
    print("C")
if mks >= 61 and mks <= 70:
    print("D")
if mks >= 0 and mks <= 60:
    print("FAIL")
else:
    print("Invalid input")
"""
Output (Type - 1)-
A
Invalid input
"""


"""
NOTE:- When we write multiple elif condition and interpreter finds or satisfy
in 1st(if) condition(Type -1) it won't check further elif's so for type-2 python will check
all (if's)conditions that's why there will be 2 answers it will print A & Invalid input.
"""
