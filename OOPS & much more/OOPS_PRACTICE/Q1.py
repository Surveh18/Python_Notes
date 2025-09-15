"""
1. Simple Class Creation
Create a class called Book that takes title and author as arguments during initialization.
Write a method that prints out the book info in a readable format.
"""


class Book:
    def __init__(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter book author: ")

    def info(self):
        print(f"Book title: {self.title}\nBook Author: {self.author}")


p1 = Book()
p1.info()
