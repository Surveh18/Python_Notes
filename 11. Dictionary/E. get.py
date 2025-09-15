marks = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "married": None,
}
# GET
# IF key exist returns the value if not then return None.
x = marks.get("sci")
print(x)  # 78

# nother way to get
m = "married"
if m in marks:
    print(marks[m])
else:
    print("Key does not exists")
# None

# Trick - we know that in get if the key dosent exists bydefault it returns None we can change that
# If key exists
x = marks.get("sci", -1)
print(x)  # 78

# If key Not exists
x1 = marks.get("scie", "kuch bhi")
print(x1)  # -1
