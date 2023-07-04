#!/usr/bin/python3

"""A definition of a rectangle class"""

class Rectangle:
    """A rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            [rect.append("#") for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return rect

    def __del__(self):
        """Print a message for every deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
