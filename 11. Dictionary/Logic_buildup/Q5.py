"""
Q5. data = {"a": 1, "b": 2, "c": 3}
👉 Approach likho: kaise dictionary ko reverse karoge
(swap key → value, value → key)?
"""

data = {"a": 1, "b": 2, "c": 3}
new_data = {}
for i, j in data.items():
    new_data[j] = i
print(new_data)
# {1: 'a', 2: 'b', 3: 'c'}
