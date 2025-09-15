# Static & class method

from datetime import datetime


class Calender:
    def __init__(self):
        self.events = []

    def add_event(self, event_name):
        self.events.append(event_name)

    def display_event(self):
        print(f"Events = {self.events}")

    @staticmethod
    def is_weekend(date: datetime):
        if date.weekday > 4:
            print("Its a weekend")
        else:
            print("Its a weekday")


"""
yha static method class k andr likha hai pr class k variables ko access nhi kr skta.
cause self nhi likha hai is_weekend parameters mai or likhte bhi nhi 
"""


obj1 = Calender()
obj1.add_event("DSA")
obj1.add_event("Party")
obj1.add_event("Cool")
obj1.display_event()
