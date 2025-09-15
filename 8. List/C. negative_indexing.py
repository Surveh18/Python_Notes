# Neagtive indexing is only in python.
lst = [5, 9, -55, 22, 9, 8, 6, 3]
# -ve indexing = [5(-8), 9(-7), -55(-6), 22(-5), 9(-4), 8(-3), 6(-2), 3(-1)]
print(lst[-3])  # 8
print(lst[-1])  # 3
n = len(lst)  # len of list is 8
print(lst[-n])  # 5
# print(lst[n])  # IndexError: list index out of range

"""
* To print middle element of list
list indexing should always in interger so we will perform
n//2 -> 50(int value)
n/2 -> 50.0(float value)
"""
print(lst[n // 2])
