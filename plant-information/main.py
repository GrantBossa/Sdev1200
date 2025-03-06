#
# Grant Bossa
# March 4, 2025
# Plant Information Programming Project
# SDEV 1200
#

# Instructions :
"""
Given a base Plant class and a derived Flower class, write a program to create a list called my_garden. 
Store objects that belong to the Plant class or the Flower class in the list. 
Create a function called print_list(), that uses the print_info() instance methods defined in the 
respective classes and prints each element in my_garden. The program should read plants or flowers 
from input (ending with -1), add each Plant or Flower to the my_garden list, and output each element 
in my_garden using the print_info() function.

Note: A list can contain different data types and also different objects.

Ex. If the input is:

plant Spirea 10  flower Hydrangea 30 false lilac  flower Rose 6 false white plant Mint 4 -1

the output is:

Plant 1 Information: Plant name: Spirea Cost: 10

Plant 2 Information: Plant name: Hydrangea Cost: 30 Annual: false Color of flowers: lilac

Plant 3 Information: Plant name: Rose Cost: 6 Annual: false Color of flowers: white

Plant 4 Information: Plant name: Mint Cost: 4
"""

import plant


def print_list(process_list):
    # Display information saved in my_garden
    print("--------------------------------")
    print("Here are the plants in my garden")
    print("--------------------------------")
    for i in range(len(process_list)):
        print(f"Plant {i+1} Information: ", end=" ")
        process_list[i].print_info()
        print(f"\n")


def main():
    # Initial Variables
    my_garden = []

    type = ""
    name = ""
    cost = 0.0
    annual = ""
    annual_yn = False
    flower_color = ""

    # Get data attributes for these classes.
    while type != "-1":
        print("------------------------------------------")
        type = input("Plant or Flower? (-1 to Quit entry): ")
        if type == "-1":
            continue
        elif type.lower() == "plant" or type.lower() == "flower":
            name = input("Plant Name: ")
            cost = float(input("Plant Cost: $ "))
        else:
            print("You entered an invalid entry, Please retry ")
            continue
        if type.lower() == "plant":
            # Create an instance of Plant class
            my_plant = plant.Plant(name, cost)
        elif type.lower() == "flower":
            # Enter flower information
            annual = input("Is this flower an Annual? (y/n): ")

            # Set annual_yn to boolean value based on input
            # Response if in case Yes, or No were answered as well
            annual_yn = True if annual[0:1].lower() == "y" else False

            # Enter flower color
            flower_color = input("Please enter the flower's color?: ")

            # Create an instance of Flower class
            my_plant = plant.Flower(name, cost, annual_yn, flower_color)

        # Add my_plant to my_garden list
        my_garden.append(my_plant)

    print_list(my_garden)


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
