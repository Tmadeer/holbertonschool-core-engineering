#!/usr/bin/env python3
def pow(a, b):
    """Computes and returns the value of a raised to the power of b."""
    result = 1
    exponent = abs(b)

    for _ in range(exponent):
        result *= a

    if b < 0:
        return 1 / result
    return result
