#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) > n:
        str1 = str[0:n:] + str[n+1::]
     print("{}".format(str1))
