#!/usr/bin/python3
""" 0x0A. Prime Game """


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(y):
    """Return a list of prime numbers up to y."""
    return [num for num in range(2, y + 1) if is_prime(num)]


def isWinner(x, nums):
    """Determine the winner of prime game"""
    if not x or not nums:
        return None
    mariaScore = 0
    benScore = 0
    for i in range(x):
        if nums[i] == 1:
            benScore += 1
        else:
            if (len(primes_up_to(nums[i]))) % 2 == 0:
                benScore += 1
            else:
                mariaScore += 1
    if mariaScore > benScore:
        return 'Maria'
    elif benScore > mariaScore:
        return 'Ben'
    else:
        return None
