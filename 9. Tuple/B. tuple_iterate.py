my_tuple = (54, 11, 13, 5, 435, 346, 5, 2312, 3432)

print(my_tuple[-1])  # 3432
print(my_tuple[3])  # 5

# via index
for i in range(0, len(my_tuple)):
    print(my_tuple[i], end=" ")
# 54 11 13 5 435 346 5 2312 3432

# via value
for j in my_tuple:
    print(j, end=" ")
# 54 11 13 5 435 346 5 2312 3432
