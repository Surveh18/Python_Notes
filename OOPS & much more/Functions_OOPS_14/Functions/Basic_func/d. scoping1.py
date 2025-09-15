def greet():
    name = "Harshal"
    print(f"Your name is {name}")


name = "xyz"  # this variable is declared outside so it can be used anywhere and also in a function - Global scope
greet()
print(name)  # this print global variable

# if i want to use global scope varible name = "xyz" it can be used with keyword Global


def treat():
    global name
    print(f"value = {name} using Global keyword.")


treat()  # this will print xyz variable.
"""
🧠 What Is Nonlocal Scope?
Nonlocal scope is when a variable lives between local and global 
— it's inside an outer function, and a nested inner function can access and 
change it using the nonlocal keyword.

🗂 Think of It Like This:
Imagine you have a notebook (the outer function) and you write down a word.
Then you open the notebook again and change that word from inside a smaller sticky note 
(the inner function). You’re not creating a new word, you’re updating the one you wrote earlier.

"""


def outer():
    sentence = "Keywords:"

    def add_keyword(word):
        nonlocal sentence
        sentence += f" {word}"

    add_keyword("Python")
    add_keyword("Django")
    add_keyword("SQL")
    print(f"Final sentence: {sentence}")


outer()
