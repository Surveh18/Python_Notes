"""
Q6. Write a Python program to convert string values of a given dictionary into
integer/float data types.
Example 1:
Original list:[
                {'x': '10', 'y': '20', 'z': '30'},
                {'p': '40', 'q': '50', 'r': '60'}
               ]
Output:[
         {'x': 10, 'y': 20, 'z': 30},
         {'p': 40, 'q': 50, 'r': 60}
        ]
Example 2:
Original list:[
                {'x': '10.12', 'y': '20.23', 'z': '30'},
                {'p': '40.00', 'q': '50.19', 'r': '60.99'}
              ]
Output:[
         {'x': 10.12, 'y': 20.23, 'z': 30.0},
         {'p': 40.0, 'q': 50.19, 'r': 60.99}
        ]
"""

Original_list = [
    {"x": "10", "y": "20", "z": "30"},
    {"p": "40", "q": "50", "r": "60"},
]


new_list = [{k: int(v) for k, v in d.items()} for d in Original_list]
print(new_list)
