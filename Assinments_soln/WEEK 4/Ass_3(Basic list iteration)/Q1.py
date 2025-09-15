"""
Q1. Make a list of your own. Print the whole list in reverse using FOR loop
and WHILE loop.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# i = len(my_list) - 1
# while i > -1:
#     print(my_list[i], end=" ")
#     i -= 1

for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end=" ")
