#!/usr/bin/python
age = input("Enter your age: ")
try:
    age = int(age)
    if age < 0:
        print("Age cannot be negative!")
    elif age > 120:
        print("That age is unlikely!")
    else:
        print("Your age is", age)
except ValueError:
    print("Error: Please enter a whole number.")
