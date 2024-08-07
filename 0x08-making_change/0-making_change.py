#!/usr/bin/python3
"""The coin change problem: a classic problem from the domain of dynamic
programming and greedy algorithms. The objective is to find the minimum number
of coins required to make up a given total amount, given a list of coin
denominations.
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total using greedy algorithm.
    coins: list of the values of the coins in your possession
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total != 0:
            count += total // coin
            total -= (total // coin) * coin

    return count if total == 0 else -1
