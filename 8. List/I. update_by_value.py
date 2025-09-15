# Replace all even numbers with zero, and odd with 1.
my_list = [54, 65, 123, 433, 3, 54, 43, 12]
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        my_list[i] = 0
    else:
        my_list[i] = 1
print(my_list)
