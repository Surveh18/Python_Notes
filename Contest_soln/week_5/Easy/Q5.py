"""
Q5. Write a Python program to map two lists into a dictionary.
Everything in both lists should be unique.
Example 1
list1 = ['red', 'green', 'blue']
list2 = ['#FF0000','#008000', '#0000FF']
Output: {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
"""

list1 = ["red", "green", "blue"]
list2 = ["#FF0000", "#008000", "#0000FF"]
result = dict()
for ch in range(0, len(list1)):
    result[list1[ch]] = list2[ch]
print(result)
# {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

result1 = {list1[ch]: list2[ch] for ch in range(len(list1))}
print(result1)
# {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

"""
🔑 Note:
[...] → list comprehension
{...} → dictionary comprehension
Assignment (=) comprehension ke andar allowed nahi hai.
if ya if...else expression allowed hai ✅
"""
