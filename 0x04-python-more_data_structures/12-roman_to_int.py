#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [dict[x] for x in roman_string] + [0]
    val = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            val += numbers[i]
        else:
            val -= numbers[i]

    return val
