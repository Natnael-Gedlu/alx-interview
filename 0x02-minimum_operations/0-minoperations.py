#!/usr/bin/python3
"""
Minimum Operations Challenge.
"""


def minOperations(n: int) -> float:
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0

    # Find factors of n
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    # Initialize dp array
    dp = [float('inf')] * (len(factors) + 1)
    dp[0] = 0

    # Calculate minimum operations
    for i in range(1, len(dp)):
        for j in range(i):
            if factors[i - 1] == factors[j]:
                dp[i] = min(dp[i], dp[j] + 1)
            else:
                dp[i] = min(dp[i], dp[j] + 2)

    return dp[-1]
