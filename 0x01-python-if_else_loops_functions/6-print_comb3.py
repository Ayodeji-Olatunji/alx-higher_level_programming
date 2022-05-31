#!/usr/bin/python3
for i in range(1, 10):
    for j in range(0, 10):
        print(
            "{}{}".format(i, j),
            end=", " if int(str(i) + str(j)) < 89 else "\n"
            )
