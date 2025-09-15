a = "Python is a great langauage"
letters = list(a)
n = len(letters)
freq_map = dict()
# for i in range(n):
#     if letters[i] in freq_map:
#         freq_map[letters[i]] += 1
#     else:
#         freq_map[letters[i]] = 1
# print(freq_map)

for i in range(n):
    freq_map[letters[i]] = freq_map.get(letters[i], 0) + 1
print(freq_map)
