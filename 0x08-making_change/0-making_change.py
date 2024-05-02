#!/usr/bin/python3
"""
Find the minimum number of coins required
from a set of various denominations to reach
a specified total amount.
"""
import sys


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to
    make change for a given total.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The total amount for which to make change.

    Returns:
        int: The minimum number of coins needed to make change for the total.
             Returns -1 if change cannot be made with the given denominations.

    Note:
        This function assumes that the denominations are given
        in decreasing order.
    """
    if total <= 0:
        return 0
    else:
        from math import trunc

        coins = sorted(coins, reverse=True)
        coin_dict = {}
        while total is not None:
            for c in coins:
                if total % c == 0:
                    coin_dict[c] = total / c
                    return int(sum(coin_dict.values()))
                else:
                    coin_dict[c] = trunc(total / float(c))
                    total -= (c * coin_dict[c])
            return -1
