#!/usr/bin/env python3
"""
Module that defines a Square class with size, position and str representation.
"""


class Square:
    """
    Class Square that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the current position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The position tuple of 2 positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character # to stdout using position.
        """
        print(self.__str__(), end="")

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: Representation of the square.
        """
        if self.__size == 0:
            return ""

        square_str = ""
        square_str += "\n" * self.__position[1]

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str[:-1]
