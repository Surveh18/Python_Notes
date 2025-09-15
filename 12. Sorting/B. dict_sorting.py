# dict_items([('Phy', 56), ('Chem', 19),
# ('Maths', 91), ('Algebra', 74), ('History', 74)])

details = {
    "Phy": 56,  # ('Phy', 56) <----x | x[1]
    "Chem": 19,
    "Maths": 91,
    "Algebra": 74,
    "History": 74,
}

print(details.items())
new_details = sorted(
    details.items(), key=lambda x: x[1]
)  # marks ki increasing value mai sort huva hai x[1]
print(new_details)
