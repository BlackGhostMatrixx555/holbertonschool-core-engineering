#!/usr/bin/env python3
"""print_matrix_integer module."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line."""
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))
