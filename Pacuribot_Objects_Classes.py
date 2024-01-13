import math


class Circle:
    def __init__(self, radius):
        # Initialize the Circle object with a given radius
        self.radius = radius

    def area(self):
        # Calculate the area of the circle using the formula A = πr^2
        circle_area = math.pi * self.radius ** 2
        # Print the calculated area with two decimal places
        print(f"Area of the circle: {circle_area:.2f}")

    def perimeter(self):
        # Calculate the perimeter (circumference) of the circle using the formula P = 2πr
        circle_perimeter = 2 * math.pi * self.radius
        # Print the calculated perimeter with two decimal places
        print(f"Perimeter of the circle: {circle_perimeter:.2f}")


# Example usage:
radius_value = 69
# Create a Circle object with the given radius
my_circle = Circle(radius_value)

# Call the area and perimeter methods to calculate and print the results
my_circle.area()
my_circle.perimeter()
