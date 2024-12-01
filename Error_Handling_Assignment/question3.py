#!/usr/bin/python
def integer_conversion():
    while True:
        user_input = input("Enter a number or type 'quit': ")
        if user_input.lower() == 'quit':
            break
        try:
            converted_number = int(user_input)
            print("The number you entered is:", converted_number)
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))