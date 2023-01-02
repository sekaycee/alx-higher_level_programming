#!/usr/bin/python3
"""
Define funtion to print a square with the character #
"""


def print_square(size):
    """ print a square with the character #
    Args:
        size: size of the square printed
    Raises:
        TypeError: If size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end='') for j in range(size)]
        print("")
