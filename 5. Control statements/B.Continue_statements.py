# Continue statement.
i = 1
while i <= 10:
    if i == 5:
        # until i becomes 5 i will not go thorugh if block rest print will execute.
        i += 1
        continue
    print(i, end=" ")
    i += 1

"""

continue baaki code ko ignore kar deta hai aur loop ke agle round mein chala jata hai.

Simple baasha mein, continue loop ke agle round ko "continue" karne ka kaam karta hai!
"""
