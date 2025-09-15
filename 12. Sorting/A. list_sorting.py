my_list = [
    ["Ani", 99],  # <---- x  |  x[1]
    ["saket", 54],
    ["paras", 21],
    ["vinayak", 45],
]
print(len(my_list))  # 4

# To access
print(my_list[1][1])  # 54
print(my_list[-1][0])  # vinayak

new_list = sorted(my_list)
print(my_list)
# [['Ani', 99], ['saket', 54], ['paras', 21], ['vinayak', 45]]
print(new_list)
# [['Ani', 99], ['paras', 21], ['saket', 54], ['vinayak', 45]]
# Ascii value k according sort huva hai u can see in keys

# If values wise sort krna ho
new2 = sorted(
    my_list, key=lambda x: x[1]
)  # <--- if x[0] means keys k according sort hoga
print(new2)
# [['paras', 21], ['vinayak', 45], ['saket', 54], ['Ani', 99]]

new3 = sorted(my_list, key=lambda x: x[1], reverse=True)
# ab reverse true hai to desending mai print hoga


# Upr jo line hai usko alag se bhi likh skte hai
def my_function(x):
    return x[1]


new4 = sorted(my_list, key=my_function, reverse=True)
