"""
User-input start(s) and end(e)

To print total of even numbers

example:
1 to 10:
2 4 6 8 10 -> total 30


"""


def even_num_sum(s, e):
    i = s
    total = 0
    while i <= e:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1


even_num_sum(1, 10)
