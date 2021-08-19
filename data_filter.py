import in_out
import star
import time
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

"""all characteristics of stars, such as RA, DEC, etc."""
characteristics = []
"""number of stars in table"""
star_cnt = 0


def sort(table: list, n: int, sort_arg: str) -> list:
    """
    Quicksort algorithm is implemented in this function,
    It takes 3 arguments: dictionary, number of stars,
    and the characteristic by which table will be sorted.
    """
    if n <= 1:
        return table
    pivot = getattr(table[n//2], sort_arg)
    left = []
    middle = []
    right = []
    for k in range(n):
        x = getattr(table[k], sort_arg)
        if x < pivot:
            left.append(table[k])
        elif x == pivot:
            middle.append(table[k])
        else:
            right.append(table[k])

    left = sort(left, len(left), sort_arg)
    right = sort(right, len(right), sort_arg)
    ans = left+middle+right
    return ans
