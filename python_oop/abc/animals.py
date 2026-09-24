#!/usr/bin/env python3
"""
This module defines the abstract Animal class and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """Class representing a Dog, inheriting from Animal."""

    def sound(self):
        """Returns the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a Cat, inheriting from Animal."""

    def sound(self):
        """Returns the sound made by a cat."""
        return "Meow"
