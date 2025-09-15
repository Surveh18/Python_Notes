# With keyword

with open("Hello.txt", "r") as f:
    print(f.read())
# If i write outside of indentation like on 6 line it throughs error
# print(f.read())

"""
Advantage of using with keyword :
1. When we go on high level things with is used
2. we dont need to close the file its automatically gets closed
"""
