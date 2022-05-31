#!/usr/bin/python3
for val in "abcdefghijklmnopqrstuvwxyz":
    if val == 'q' or val == 'e':
        continue
print("{}".format(val), end="")
