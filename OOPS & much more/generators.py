# iska kaam hota hai ek ek kr k value dena


def num():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for i in num():
    print(i, end=" ")
# 1 2 3 4 5
# its kinda type of return
print()
x = num()
print(next(x))  # 1
print(next(x))  # 2
print(next(x))  # 3
print(next(x))  # 4
print(next(x))  # 5
