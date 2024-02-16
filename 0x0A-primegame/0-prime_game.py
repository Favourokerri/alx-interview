#!/usr/bin/python3
"""
This module contains the prime game as explained in README.md
"""


def primeNumbers(n):
    """Returns prime numbers between 1 and n"""
    prime_numbers = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime_numbers.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime_numbers


def isWinner(x, nums):
    """Determines the winner of the game"""
    if x is None or nums is None or x == 0 or not nums:
        return None
    maria_score = ben_score = 0
    for n in range(x):
        prime_numbers = primeNumbers(nums[n])
        if len(prime_numbers) % 2 != 0:
            maria_score += 1
        else:
            ben_score += 1
    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
