"""
Q8. Write a Python code to split a list into two halves using list slicing.
(Keep the length of list even).
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
n = len(my_list)
first_half = my_list[: n // 2]
second_half = my_list[n // 2 :]
print(first_half)
print(second_half)
