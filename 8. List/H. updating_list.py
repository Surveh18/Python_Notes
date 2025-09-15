my_list = [45, 56, 33, 78, "Surve", True]
print(f"My List = {my_list}")
# My List = [45, 56, 33, 78, 'Surve', True]

my_list[0] = 12  # here we are updating 0 index value by 12
print(f"My List = {my_list}")
# My List = [12, 56, 33, 78, 'Surve', True]

my_list[-1] = 100  # here we are updating -1 index value by 100
print(f"My List = {id(my_list)}")
# My List = 2535550671104
