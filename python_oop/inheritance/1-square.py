#!/usr/bin/env python3
"""
This module defines the Square class inheriting from Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inherited from Rectangle."""

    def __init__(self, size):
        """Initializes a Square instance with validated size.

        Args:
            size (int): The size of the sides of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
