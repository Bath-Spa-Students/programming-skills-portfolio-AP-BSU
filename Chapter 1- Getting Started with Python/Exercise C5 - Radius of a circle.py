import math
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area
def main():
    radius = float(input("Please enter your radius value: "))
    if radius < 0:
        print("Value and radius cannot be negative.")
    else:
        area = calculate_circle_area(radius)
        print(f"Area of the circle with radius {radius} is {area:.2f}")
        print(f"The equation of the circle is: x^2 + y^2 = {radius**2:.2f}")
if __name__ == "__main__":
    main()
