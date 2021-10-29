#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program translates strings into unicode characters

import constants


def hexa_decimal(user_input):
    my_characters = []
    unicodes = ""

    for unicodes in user_input:
        if unicodes in constants.DICTIONARY.keys():
            my_characters.append(constants.DICTIONARY[unicodes])
    
    return my_characters


def main():
    # this function uses an associative array

    # input
    user_input = input("Enter a string to be translated into hex: ")

    # call functions
    final_answer = hexa_decimal(user_input)

    # output
    print("\n{0} in hexa is {1}.".format(user_input, final_answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
