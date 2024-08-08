#!/usr/bin/python3
""" 0x0A. Prime Game """


def primes_up_to(limit):
    """Generate list of primes up to limit"""
    primeNumbers = []
    sieveList = [True] * (limit + 1)
    for potentialPrime in range(2, limit + 1):
        if sieveList[potentialPrime]:
            primeNumbers.append(potentialPrime)
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False
    return primeNumbers


def isWinner(x, nums):
    """Determine the winner of prime game"""
    if not x or not nums:
        return None
    mariaScore = 0
    benScore = 0
    for i in range(x):
        if nums[i] == 0:
            continue
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
