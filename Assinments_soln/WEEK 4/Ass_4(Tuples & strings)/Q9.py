"""
Q9.
Write a python program to only print second half of the string. Ask string from user.
1. Example string: aeroplane
Output: lane

2. Example string: delhi
Output: hi

3. Example string: pavbhaji
Output: aji

"""


def seconHalfString(n: str):
    return n[len(n) // 2 + 1 : :]


print(seconHalfString("aeroplane"))  # lane
print(seconHalfString("delhi"))  # hi
print(seconHalfString("pavbhaji"))  # aji
