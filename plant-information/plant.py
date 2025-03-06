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


# A class named `Plant` that holds the attributes: name, cost as well as print_info() to display these.
class Plant:
    # The __init__method initalizes the attributes.
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    # The set_name method assigns a value to the `__name` field.
    def set_name(self, name):
        self.__name = name

    # The set_cost method assigns a value to the `__cost` field.
    def set_cost(self, cost):
        self.__cost = round(cost, 2)

    # The get_name method returns the value of the `__name` field.
    def get_name(self):
        return self.__name

    # The get_cost method returns the value of the `__cost` field.
    def get_cost(self):
        return self.__cost

    # The print_info() method returns the value of the fields in this class.
    def print_info(self):
        print(f"Plant name: {self.__name} Cost: $ {self.__cost:.2f}", end=" ")


# A class named `Flower` that holds the parent attributes: name, cost
# as well as attributes: annual_yn, flower_color and includes a print_info() to display these.
class Flower(Plant):
    # The __init__method initalizes the attributes.
    def __init__(self, name, cost, annual_yn, flower_color):
        # call the superclass __init__ method
        Plant.__init__(self, name, cost)
        self.__annual_yn = annual_yn
        self.__flower_color = flower_color

    # The set_annual_yn method assigns a value to the `__annual_yn` field.
    def set_annual_yn(self, annual_yn):
        self.__annual_yn = annual_yn

    # The set_flower_color method assigns a value to the `__flower_color` field.
    def set_flower_color(self, flower_color):
        self.__flower_color = flower_color

    # The get_annual_yn method returns the value of the `__annual_yn` field.
    def get_annual_yn(self):
        return self.__annual_yn

    # The get_flower_color method returns the value of the `__flower_color` field.
    def get_flower_color(self):
        return self.__flower_color

    # The print_info() method returns the value of the fields in this class.
    def print_info(self):
        super().print_info()
        print(
            f"Annual: {self.__annual_yn} Color of flowers: {self.__flower_color}",
            end=" ",
        )
