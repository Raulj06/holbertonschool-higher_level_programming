#!/usr/bin/python3
   """ module with rectangle class """


   BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle defined """

    def __init__(self, width, height):
        """ Comment """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height
