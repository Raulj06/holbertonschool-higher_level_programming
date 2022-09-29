#!/usr/bin/python3
    """ module basegeometry class """


class BaseGeometry:
    """ BaseGeometry defined """

    def area(self):
    raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
    if type(value) in not an int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0.".format(name))
