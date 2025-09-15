def marks(m1, m2):
    total = m1 + m2
    return total


x = marks(2, 4)
print(x)


# def subject(s1, s2):
#     total = s1 + s2
#     print(
#         f"total = {total}"
#     )  # here we are printing total but it is not returning the total value to the function.


# The flow of program will be firstly x = subjects(5,6) the it will read the function.
# then print(x)
# x = subject(5, 6)
# print(f"value of x = {x}")
# when we dont store anything in variable it will consider as none datatype.
# Check test.py
# Now to overcame this situation we will use annonation.


def minus(a: int, b: int) -> str:
    total = a - b
    return f"Your marks is {total}"


x = minus(10, 2)  # once hover on minus.
print(f"x = {x}")
