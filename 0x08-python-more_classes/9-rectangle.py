#!/usr/bin/python3
"""
    Module defining rectangle
    return {}
"""


class Rectangle():
    """rectangle class"""

    # A class variable, counting the number of rectangles
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Return Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return Rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @property
    def width(self):
        """Retrieve width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Print the rectangle with the char #"""
        if self.__height == 0 or self.__width == 0:
            return("")
        else:
            str1 = ""
            for x in range(self.__height):
                for y in range(self.__width):
                    str1 += str(self.print_symbol)
                str1 += "\n"
        return(str1[:-1])

    def __repr__(self):
        """Get string evaluation of the rectangle"""
        if self.__height == 0 or self.__height == 0:
            return("Rectangle()")
        else:
            return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Prints when the instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Return rectangle with the largest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Return rectangle instance as square"""
        return Rectangle(size, size)
