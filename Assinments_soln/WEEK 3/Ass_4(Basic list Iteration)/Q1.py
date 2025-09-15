"""
Q1. Make a list of your own. Print the whole list in reverse using FOR loop
and WHILE loop.
"""

own_list = [1, 566, -9, "Surve", "iphone", 0.877]
n = len(own_list)
for i in range(n - 1, -1, -1):
    print(own_list[i], end=" ")
print()

i = n - 1
while i >= -1:
    print(own_list[i], end=" ")
    i -= 1
