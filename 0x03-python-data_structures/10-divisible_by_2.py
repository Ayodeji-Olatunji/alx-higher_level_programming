#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    my_list_2 = [True if num % 2 == 0 else False for num in my_list]
    return my_list_2
