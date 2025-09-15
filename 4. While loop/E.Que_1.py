"""
User_input Start & End are 2 variables.

We have to print from start to end.

Example:
Start = 6
End = 11
O/p-6 7 8 9 10 11

"""

# start = int(input("Enter Start_num: "))
# end = int(input("Enter Start_num: "))


def start_end(start, end):
    while start <= end:
        print(start, end=" ")
        start += 1


# Alternate soln

# i = start
# while i <=end:
#     print(i,end=" ")
#     i += 1

start_end(start=6, end=11)
