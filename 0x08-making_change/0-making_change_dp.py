#!/usr/bin/python3
"""The coin change problem: a classic problem from the domain of dynamic
programming and greedy algorithms. The objective is to find the minimum number
of coins required to make up a given total amount, given a list of coin
denominations.
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total using dynamic programming.
    coins: list of the values of the coins in your possession
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    amounts = [total + 1] * (total + 1)
    amounts[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                amounts[i] = min(amounts[i], amounts[i - coin] + 1)

    return amounts[total] if amounts[total] <= total else -1
