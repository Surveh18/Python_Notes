"""
marks = {"Math": 90, "Science": 80, "English": 70}
👉 Approach likho: kaise sirf subjects ke naam print karoge,
 aur kaise sirf marks print karoge?
"""

# Q1 Type-1
marks = {"Math": 90, "Science": 80, "English": 70}
for i in marks.keys():
    print(i, end=" ")
# Math Science English
print()
for values in marks.values():
    print(values, end=" ")
# 90 80 70
