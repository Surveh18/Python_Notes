my_list = [5, 9, -55, 22, 9, 8, 6, 3]
# indexing = [5(0), 9(1), -55(2), 22(3), 9(4), 8(5), 6(6),3(7)]
print(my_list[3])  # 22
print(my_list[0])  # 5
print(my_list[7])  # 3
# print(my_list[9])  # IndexError: list index out of range
print(f"length of list = {len(my_list)}")
# length of list = 8

"""
Question: suppose we dont know that how many elements are there in list
and i want to print the last element.
"""
L = len(my_list)  # len of list is stored in L variable
print(my_list[L - 1])  # here we are print my_list in sqaure bracket element.
# 3
print(my_list[len(my_list) - 1])  # short hand(in one line).
