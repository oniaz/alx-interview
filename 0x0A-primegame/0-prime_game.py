#!/usr/bin/python3
""" 0x0A. Prime Game """


def count_primes_up_to(n):
    """
    Counts prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n: The upper limit for prime number generation.

    Returns:
        Number of prime numbers up to n.
    """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    prime_count = 0
    for p in range(2, n+1):
        if prime[p]:
            prime_count += 1

    return prime_count


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
            if (count_primes_up_to(nums[i])) % 2 == 0:
                benScore += 1
            else:
                mariaScore += 1
    if mariaScore > benScore:
        return 'Maria'
    elif benScore > mariaScore:
        return 'Ben'
    else:
        return None
