# You have given an arry it can contain duplicates then remove duplicates.
arr = [32, 56, 2, 76, 65, 32, 32, 32, 89, 11]
result = []
x = 32
for num in arr:
    if num != x:
        result.append(num)
print(result)
