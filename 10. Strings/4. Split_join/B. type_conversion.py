my_list = [334, 54, 56, 54, 432, "Anirudh"]
# List to str
print(str(my_list))  # '[334, 54, 56, 54, 432, 'Anirudh']'
print(str(my_list)[0])  # [
print(str(my_list)[3])  # 4
print(str(my_list)[-1])  # ]

a = "python is a good language"
lst = list(a)  # str -> list
print(lst)
"""
['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e'] 
"""
for i in range(0, len(lst)):
    if lst[i] == "o":
        lst[i] = "z"
print(lst)
# ['p', 'y', 't', 'h', 'z', 'n', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'z', 'z', 'd', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
print("".join(lst))
# pythzn is a gzzd language
