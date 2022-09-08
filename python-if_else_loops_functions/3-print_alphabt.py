#!/usr/bin/python3
import string
for i in range(ord('a'), ord('z')+1):
    if i == ord('e') or i == ord('q'):
    continue
    print("{:c}".format(i), end="")
