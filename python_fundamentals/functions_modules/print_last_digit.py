#!/usr/bin/env python3
def print_last_digit(number):
    """Print and return the last digit of number (always positive)."""
    digit = abs(number) % 10
    print(digit)
    return digit
