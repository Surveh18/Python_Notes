# like how we take a slice of cake its like this
arr = [54, 67, 54, 12, 33, 44, 33, 10]
result = []
# suppose we want 1st 3 elements of arr
# Method 1 - Using for loop
for i in range(0, 3):
    result.append(arr[i])
print(result)
# [54, 67, 54]

# Method 2 - Using list slicing
# arr = [start:stop:step] by default step is 1
# If step is +ve it moves in (->) , if step is -ve it moves in (<-)
# result = arr[0:3]
# result = arr[0:6]
# result = arr[5:2:-1]
# result = arr[-7:-4]
# result = arr[3 : len(arr)]
# result = arr[3:]
# result = arr[3::-1]
# result = arr[:]
result = arr[::-1]
print(result)
