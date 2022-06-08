#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_dict = sorted(a_dictionary)

    for i in ordered_dict:
        print('{}: {}'.format(i, a_dictionary[i]))
