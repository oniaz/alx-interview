#!/usr/bin/python3
"""
Calculate the fewest number of operations needed to print n H characters.
"""
import math


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def minOperations(n):
    """
    Calculate the fewest number of operations needed to print n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible
            to achieve.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if is_prime(n):
        return n

    # Find the smallest factor of n greater than 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return minOperations(i) + minOperations(n // i)

    return n  # If n is prime, it wasn't caught by the above check
