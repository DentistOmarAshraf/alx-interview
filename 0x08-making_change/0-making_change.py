#!/usr/bin/python3
"""
makeChange - function count coins from total
"""


def makeChange(coins, total):
    """makeChange
    """
    if total == 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coins = 0
    startMoney = total

    for coin in sorted_coins:
        temp_result = startMoney // coin
        coins += temp_result
        startMoney -= temp_result * coin

    if startMoney > 0:
        return -1
    return coins
