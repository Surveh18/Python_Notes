"""
Q2. Given two dictionaries, write a function to merge them into a new dictionary.
If there is any overlap of keys, the value from the second dictionary should
overwrite the one from the first dictionary.
Dictionary 1:
{'apple': 3, 'banana': 5, 'cherry': 7}
Dictionary 2:
{'banana': 8, 'orange': 10, 'apple': 9}
Expected Output:
{'apple': 9, 'banana': 8, 'cherry': 7, 'orange': 10}
"""


def merged(dict1: dict, dict2: dict):
    merge = dict1.copy()
    merge.update(dict2)
    return merge


dict1 = {
    "apple": 3,
    "banana": 5,
    "cherry": 7,
}
dict2 = {
    "banana": 8,
    "orange": 10,
    "apple": 9,
}
print(merged(dict1, dict2))
