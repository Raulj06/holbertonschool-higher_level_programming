#!/usr/bin/python3
   """ module function """


def read_file(filename=""):
    """ read_file defined """
    with open(filename) as f:
        for line in f:
            print(line, end="")
