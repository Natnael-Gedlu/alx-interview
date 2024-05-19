#!/usr/bin/python3
"""
This module determines the winner of a game based on given numbers.
"""


def isWinner(x, nums):
    """
    Determines the game winner.
    x (int): Number of rounds.
    nums (list): List of integers.

    Returns:
    str: "Ben", "Maria", or None.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    max_num = sorted(nums)[-1]
    primes = [1 for _ in range(max_num + 1)]
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        rm_multiples(primes, i)

    for i in nums:
        if sum(primes[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(primes, x):
    """
    Marks multiples of a number as non-prime.
    primes (list): List indicating prime status.
    x (int): Number whose multiples are marked.

    """
    for i in range(2, len(primes)):
        try:
            primes[i * x] = 0
        except IndexError:
            break
