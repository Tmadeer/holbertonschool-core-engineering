#!/usr/bin/env python3
"""
This module defines abstract Shape class, Circle, Rectangle and shape_info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate shape perimeter."""
        pass


class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initializes a Circle with a radius.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes a Rectangle with width and height.

        Args:
            width (int or float): The width of the rectangle.
            height (int or float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing.

    Args:
        shape (object): An object that implements area() and perimeter().
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
