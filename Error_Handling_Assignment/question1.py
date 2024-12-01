#!/usr/bin/python
def division_calculator():
    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            
            if denominator == 0:
                print("Error: Denominator cannot be zero.")
            else:
                print("The result is:", numerator / denominator)
                break
        except ValueError:
            print("Error: Please enter whole numbers.")
