"""
Q11. Given a dictionary with key-value pairs, remove all the keys with values
greater than K, including mixed values.

Input : test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'xyzx' : 'CS'},
K = 7
Output : {'Gfg' : 3, 'for' : 6, 'xyzx' : 'CS'}
Explanation : All values greater than K are removed.
Mixed value is retained.

Input : test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'qqqq' : 'CS'},
K = 1
Output : {'qqqq' : 'CS'}
Explanation : Only Mixed value is retained

"""

test_dict = {
    "Gfg": 3,
    "is": 7,
    "best": 10,
    "for": 6,
    "xyzx": "CS",
}
K = 1

# Create a new dictionary to avoid modifying dict while iterating
filtered_dict = {
    key: value
    for key, value in test_dict.items()
    if not (isinstance(value, int) and value > K)
}

print(filtered_dict)
