#!/usr/bin/python3
"""The coin change problem: a classic problem from the domain of dynamic
programming and greedy algorithms. The objective is to find the minimum number
of coins required to make up a given total amount, given a list of coin
denominations.
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    coins: list of the values of the coins in your possession
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
