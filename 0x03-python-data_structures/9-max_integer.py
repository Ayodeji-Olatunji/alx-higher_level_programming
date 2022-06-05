#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        max_num = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] > max_num:
                return my_list[i]
    else:
        return None
