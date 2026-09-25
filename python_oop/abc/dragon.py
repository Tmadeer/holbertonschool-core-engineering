#!/usr/bin/env python3
"""
This module defines SwimMixin, FlyMixin, and the Dragon class.
"""


class SwimMixin:
    """Mixin class that adds swimming capability."""

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying capability."""

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints dragon roaring sound."""
        print("The dragon roars!")
