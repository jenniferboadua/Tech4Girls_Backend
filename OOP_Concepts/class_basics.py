class Car:
    def __init__(self, make, model, year):
        # Initialize instance variables
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        # print the car details
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
        #create an instance of the car
        car_1= Car("Toyota", "Camry", "2024")
        car_1.display_info()