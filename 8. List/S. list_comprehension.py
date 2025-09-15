# To create a new list
# If we have to add 1-10 num in a list
# Example - 1
# Method -1 regular method
result = []
for i in range(1, 11):
    result.append(i + 5)
print(result)
# [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Method - 2 Using list comprehension
result1 = [i + 5 for i in range(1, 11)]
print(result1)
# [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Example - 2
result3 = []
for i in range(1, 11):
    if i % 2 == 0:
        result3.append("Even")
    else:
        result3.append("Odd")
print(result3)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

result4 = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
print(result4)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

#        kya add krna hai                kab add krna hai
#               ↓                               ↓
# result1 = [(i + 5) for i in range(1, 11) (if i % 2 == 0)]

# Example - 3
result5 = []
for i in range(1, 11):
    if i % 2 == 0:
        result5.append(i)
print(result5)
# [2, 4, 6, 8, 10]

result6 = [i for i in range(1, 11) if i % 2 == 0]
print(result6)
# [2, 4, 6, 8, 10]

# Question = convert list string into integers
arr = ["22", "33", "32", "78", "12"]
final = [int(i) for i in arr]
print(final)
# [22, 33, 32, 78, 12]
