#
# Grant Bossa
# March 13, 2025
# Recursive Multiplication Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.


def recurse_multiply(x, y):
    # Test for zero values
    if x == 0 or y == 0:
        return 0
    # Test for non-recursive values
    if x == 1:
        return y
    if y == 1:
        return x
    # Process recursive values
    if x > 1:
        return y + recurse_multiply(x - 1, y)


def main():
    # Enter x and y values
    x, y = map(int, input("Please enter the X and Y values in the format x, y: ").split(", "))
    
    z = recurse_multiply(x, y)
    
    print(f"The value is {z}") non


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
