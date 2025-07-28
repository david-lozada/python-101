# Day 3: 30 Days of python programming
import math

"""age = 27
height = 1.70
example = 3 + 4j

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base * height
print(f"The area of the triangle is: {area_of_triangle}")"""

"""side_a = int(input("Enter the length of side a: "))
side_b = int(input("Enter the length of side b: "))
side_c = int(input("Enter the length of side c: "))
triangle_perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is: {triangle_perimeter}")"""

"""length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"area : {area} and perimeter: {perimeter}")"""

"""circle_radius = float(input("Enter the radius of the circle: "))
area = math.pi + circle_radius ** 2
circunference = 2 * math.pi * circle_radius
print(f"Area: {area:.2f} and Circumference: {circunference:.2f}")"""

"""hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
salary = hours * rate_per_hour
print(f"Your weekly earning is: {salary}")"""

"""SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
SECONDS_PER_DAY = SECONDS_PER_HOUR * 24
SECONDS_PER_YEAR = SECONDS_PER_DAY * 365
MAX_LIFESPAN_YEARS = 100

# Calculate seconds in the given years (cap at 100 years)
years = int(input("Enter your age in years: "))
years = min(years, MAX_LIFESPAN_YEARS)
total_seconds = years * SECONDS_PER_YEAR
print(f"A person can live {total_seconds:,} seconds in {years} years.")"""

rows = 5

# Print header
print("n 1 n n² n³")

# Generate and print each row
for n in range(1, rows + 1):
    print(f"{n} 1 {n} {n**2} {n**3}")