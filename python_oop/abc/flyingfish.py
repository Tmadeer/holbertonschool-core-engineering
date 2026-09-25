#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Prints fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Prints bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a FlyingFish, inheriting from Fish and Bird."""

    def fly(self):
        """Overrides fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")
