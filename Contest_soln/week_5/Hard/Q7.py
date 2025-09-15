"""
Q7. Convert a list of Tuples into Dictionary
Input: [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
Output: {'akash': [10], 'gaurav': [12], 'anand': [14], 'ashish': [30], 'akhil': [25], 'suraj': [20]}
Input: [('A', 1), ('B', 2), ('C', 3)]
Output: {'B': [2], 'A': [1], 'C': [3]}
"""

# Example input
tuples_list = [
    ("akash", 10),
    ("gaurav", 12),
    ("anand", 14),
    ("suraj", 20),
    ("akhil", 25),
    ("ashish", 30),
]

# Initialize empty dictionary
result_dict = {}

# Loop through each tuple
for t in tuples_list:
    key = t[0]
    value = t[1]
    result_dict[key] = [value]  # Make the value a list

print(result_dict)
