import datetime


def show_age(birth):
    thisyear = datetime.datetime.now().year
    age = thisyear - birth
    print(f"You are {age} years old")


show_age(int(input("Enter your birth year : ")))
