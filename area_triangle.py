#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: November 23 2022
# This program calculates the area of a triangle


def calculate_area(height, base):
    # calculate area

    # process
    area = (height * base)/2

    # output
    print("The area is {0} cm²".format(area))

def main():
    # this function gets length and width

    # input
    height_from_user_string = input("Enter the height of a rectangle (cm): ")
    base_from_user_string = input("Enter the base of a rectangle (cm): ")
    print("")

    try:
        # converts string to float
        height_from_user_float = float(height_from_user_string)
        base_from_user_float = float(base_from_user_string)
        # makes sure input is greater than 0
        if base_from_user_float > 0 and height_from_user_float > 0:
            # call functions
            calculate_area(height_from_user_float, base_from_user_float)
        else:
            print("The base and height must be greater than 0.")
    # checks if the number is a string
    except Exception:
        print("Invalid data entered! Only numbers can be accepted!")


if __name__ == "__main__":
    main()