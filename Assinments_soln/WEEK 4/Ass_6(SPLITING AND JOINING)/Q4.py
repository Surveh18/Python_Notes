"""
Q4.Ask 5 integers from user. Then ask a single character from user.
Print those integers separated by that character entered by user.

"""

nums = []  # store numbers
for i in range(4):
    n = input("Enter num: ")
    nums.append(n)

char = input("Enter char: ")
result = char.join(nums)
print(result)
