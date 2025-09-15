# Map means key-value pair although dict is used for mapping.
# As we storing frequency as value we have use variable name frequency map.
arr = [5, 9, 5, 3, 3, 3, 2, 1, 9, 9, 1, 5]
freq_map = dict()
n = len(arr)
for i in range(n):
    if arr[i] in freq_map:
        freq_map[arr[i]] += 1
    else:
        freq_map[arr[i]] = 1
print(
    freq_map,
)

# Method 2
# for i in range(n):
#     freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
# print(freq_map)

# from collections import Counter

# Method 3 - in one line.
# arr = [5, 9, 5, 3, 3, 3, 2, 1, 9, 9, 1, 5]
# freq_map = dict(Counter(arr))
# print(freq_map)
# print(Counter(arr))
