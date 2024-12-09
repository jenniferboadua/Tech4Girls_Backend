class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(length: {self.length}, width: {self.width})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.length * self.width == other.length * other.width
        


# Create instances of Rectangle
rect1 = Rectangle(6, 4)
rect2 = Rectangle(5, 7)

# Print details and compare rectangles
print(rect1)
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")

print(rect2)
print(f"Area: {rect2.area()}")
print(f"Perimeter: {rect2.perimeter()}")

# Check if the two rectangles are equal
print(f"Are rect1 and rect2 equal? {rect1 == rect2}")
