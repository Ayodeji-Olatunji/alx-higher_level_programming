#!/usr/bin/python3
def print_last_digit(number):
    return number % 10 if number > 0 else int(repr(number[-1])) * -1
