class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)  # Call the parent class constructor
        self.department = department

    def get_details(self):
        # Override the get_details method to include department
        super().get_details()  # Call the parent class method
        print(f"Department: {self.department}")


# Create instances of Employee and Manager
emp = Employee("Jennifer", "Software Engineer")
mgr = Manager("Kiss", "Leader", "IT")

# Display their details
emp.get_details()
mgr.get_details()
