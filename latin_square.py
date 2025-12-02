"""
latin_square.py
----------------
Utility functions to generate k × k Latin Squares.

This module provides:
- A simple base Latin square generator
- A permutation-based generator for randomness
"""

import random
from typing import List


def generate_latin_square(k: int, seed: int | None = None) -> List[List[int]]:
    """
    Generate a k × k Latin square using modular addition.

    Args:
        k (int): Size of the square.
        seed (int, optional): If provided, randomizes row/column permutations.

    Returns:
        List[List[int]]: A Latin square where each number 0..k-1
                         appears exactly once in each row and column.
    """
    square = [[(i + j) % k for j in range(k)] for i in range(k)]

    if seed is not None:
        random.seed(seed)
        random.shuffle(square)                # shuffle rows
        cols = list(range(k))
        random.shuffle(cols)
        square = [[row[c] for c in cols] for row in square]  # shuffle columns

    return square
