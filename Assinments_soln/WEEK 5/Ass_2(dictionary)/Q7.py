"""
Q7. Write a Python function that takes a dictionary as input where
the values are lists of integers. The function should return a new
dictionary where the values are lists containing only the even integers
from the original lists.

Input_dict = {
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8],
}
Output = {
    "A":[2,4],
    "B":[6,8],
}

"""


def filter_even(input_dict: dict) -> dict:
    output_dict = {}
    for key, values in input_dict.items():  # traverse dictionary
        output_dict[key] = [v for v in values if v % 2 == 0]  # filter even numbers
    return output_dict


# Example
Input_dict = {
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8],
}

print(filter_even(Input_dict))
