#!/usr/bin/python
data = {"name": "Alice", "age": 25, "country": "Wonderland"}

def dictionary_lookup():
    while True:
        key = input("Enter key you want to lookup or type 'q' to quit: ")
        if key.lower() == 'q':
            break
        if key in data:
            print("Value:", data[key])
        else:
            print(f"Error: Key '{key}' not found in the dictionary.")
            print("Available keys:", list(data.keys()))