#!/usr/bin/python3
for i in range(0, 10):
    for d in range(i + 1, 10):
        if d > i:
            print("{}{}".format(i, d))
        else:
            print("{}{}".format(i, d), end="") 
