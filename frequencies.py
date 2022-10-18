"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    items_str = [str(item) for item in items]
    frequencies = {}
    for item in items_str:
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1

    return frequencies
