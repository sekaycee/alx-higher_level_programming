#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    number %= 10
    print(number, end='')
    return(number)
