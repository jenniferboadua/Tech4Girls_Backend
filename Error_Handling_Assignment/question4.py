#!/usr/bin/python
items = ["apple", "banana", "cherry"]

def access_list():
    while True:
        index = input("Enter the index of the item you want to access or type 'quit' to quit: ")
        if index.lower() == 'quit':
            break
        try:
            index = int(index)
            if index < 0 or index >= len(items):
                print("Error: Index out of bounds.")
            else:
                print("You selected:", items[index])
        except ValueError:
            print("Error: Invalid input.")
