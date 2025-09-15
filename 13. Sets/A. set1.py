# set data type, to store unique value
# Mutable - means i can add anything
# Unordered
# No indexing
my_set = {1, 4, 4, 1, 1, 1, 3, 5, 7, "How", 76.44}
print(my_set)
# {1, 3, 4, 5, 'How', 7, 76.44}
# Unique aayenge values plus unorder hrr baar run karo change hota hai

my_set.add(100)  # randomly kahi bhi add hjaayega
print(my_set)
# {1, 3, 4, 5, 100, 7, 76.44, 'How'}

my_set.remove(1)
print(my_set)
# {'How', 3, 4, 5, 100, 7, 76.44}

