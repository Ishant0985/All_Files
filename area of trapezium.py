def trapezium_area(base1, base2, height):
    """Calculates the area of a trapezium.

    Args:
        base1: The length of the first base.
        base2: The length of the second base.
        height: The height of the trapezium.

    Returns:
        The area of the trapezium.
    """

    area = 0.5 * (base1 + base2) * height
    return area

# Get input from the user
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezium: "))

# Calculate and print the area
area = trapezium_area(base1, base2, height)
print("The area of the trapezium is:", area)
