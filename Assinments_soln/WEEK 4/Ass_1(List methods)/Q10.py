"""
Q10. Ask 10 numbers from the user and put them into a list.Now remove all the 
even numbers from that list.
"""

num = []
for i in range(10):
    nums = int(input(f"Enter num {i+1}: "))
    if num == 0:
        break
    num.append(nums)

filtered_num = []
for j in num:
    if j % 2 != 0:
        filtered_num.append(j)
print(f"List after removing even number {filtered_num}")
