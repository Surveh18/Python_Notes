"""
Q3. Make a list of your own. Count how many numbers are divisible by 5.
"""

my_list = [54, 67, 1, 43, 67, 100, 45, 32, 74, 51, 40]
count = 0
# for i in my_list:
#     if i % 5 == 0:
#         count += 1
# print(count)

for i in range(0, len(my_list)):
    if my_list[i] % 5 == 0:
        count += 1
print(count)
