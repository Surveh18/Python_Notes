"""
Q7.Write a function that returns the string "something" joined with a
space " " and the given argument a.

# Examples: 
• give_me_something("is better than nothing") "something is better than nothing"
• give_me_something("Bob Jane") -4 "something Bob Jane"
• give_me_something("something") -4 "something something"
"""


def give_me_something(a: str) -> str:
    return "something" + " " + a


print(give_me_something("is better than nothing"))
print(give_me_something("Bob Jane"))
print(give_me_something("something"))
