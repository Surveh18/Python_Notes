"""
fruits = {"apple": 100, "banana": 40, "mango": 60}
👉 Approach likho: kaise check karoge ki "banana" dictionary me hai ya nahi?
"""

fruits = {"apple": 100, "banana": 40, "mango": 60}
print(fruits["banana"])  # 40

if "banana" in fruits:
    print("Banana is present")
else:
    print("Banana is not present")
