# Pass by reference,means passing the address.
# Mutable - List is mutable.the thing which can be changed.
# Pass by ref will go under mutable.
from typing import List


def change(my_list: List):
    my_list[0] = 100


xyz = [2, 45, 89, 23, 41]
change(xyz)
print(xyz)
# Output - [100, 45, 89, 23, 41]
