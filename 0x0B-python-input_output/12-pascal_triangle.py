#!/usr/bin/python3
"""Task 12 of ALX Project(Python - Input/Output)

This module defines a Pascal's Triangle function.

"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        mostRecentLayer = triangle[-1]
        thisLayer = [1]
        for i in range(len(mostRecentLayer) - 1):
            thisLayer.append(mostRecentLayer[i] + mostRecentLayer[i + 1])
        thisLayer.append(1)
        triangle.append(thisLayer)

    return triangle
