#
# Grant Bossa
# March 13, 2025
# Recursive Multiplication Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.


def recurse(x, y):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    if x > 1:
        return y + recurse(x - 1, y)


def main():
    # Initial Variables

    x = int(input("Please enter the X value: "))
    y = int(input("Please enter the Y value: "))
    z = recurse(x, y)
    print(f"The value is {z}")


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
