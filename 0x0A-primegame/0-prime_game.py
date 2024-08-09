#!/usr/bin/python3
""" 0x0A. Prime Game """


def primes_up_to(n):
    """
    Generates a list of prime numbers up to y using the Sieve of Eratosthenes.

    Args:
        y: The upper limit for prime number generation.

    Returns:
        A list of prime numbers up to y.
    """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Create a list of prime numbers
    prime_count = 0
    # primes = []
    for p in range(2, n+1):
        if prime[p]:
            prime_count += 1
            # primes.append(p)

    return prime_count
    # if y <= 1:
    #     return []

    # primes = [True] * (y + 1)
    # primes[0] = primes[1] = False

    # for p in range(2, int(y**0.5) + 1):
    #     if primes[p]:
    #         for i in range(p * p, y + 1, p):
    #             primes[i] = False

    # return [i for i in range(2, y + 1) if primes[i]]


def isWinner(x, nums):
    """Determine the winner of prime game"""
    mariaScore = 0
    benScore = 0
    for i in range(x):
        if nums[i] == 0:
            continue
        if nums[i] == 1:
            benScore += 1
        else:
            # if (len(primes_up_to(nums[i]))) % 2 == 0:
            if (primes_up_to(nums[i])) % 2 == 0:
                benScore += 1
            else:
                mariaScore += 1
    if mariaScore > benScore:
        return 'Maria'
    elif benScore > mariaScore:
        return 'Ben'
    else:
        return None
