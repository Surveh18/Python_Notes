"""
Q2. Make a list of your owm Print all the numbers divisible by 3 and 4 in
that list.
"""

num = [54, 132, 76, 87, 231, 432, 765, 876, 2, 1, 11]
n = len(num)
for i in range(0, n):
    if num[i] % 3 == 0 and num[i] % 4 == 0:
        print(num[i], end=" ")
print()
for i in num:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
