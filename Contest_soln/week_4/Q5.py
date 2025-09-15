"""
Q5. Ask a string from user. Replace all the space characters with “-”. Do not use replace() method.
"""

# n = "Python is a good one"
# ans = n.split()
# ans1 = "-".join(ans)
# print(ans1)


def replaceSpace(n: str):
    return "-".join(n.split())


print(replaceSpace("Python is a good one"))
# Python-is-a-good-one
