#!/usr/bin/python3
def uppercase(str):
    temp = list(str)
    for s in range(len(temp)):
        if ord(temp[s]) > 96 and ord(temp[s]) < 123:
            temp[s] = chr(ord(temp[s]) - 32)
    print("{}".format("".join(tmp)))
