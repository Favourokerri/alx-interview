#!/usr/bin/python3
""" making change """


def makeChange(coins, total):
    """ fewest coin to  meet total """
    max_num = max(coins)
    number_of_coins = 0
    new_total = 0
    sorted_coin = sorted(coins, reverse=True)

    for i in range(len(sorted_coin)):
        while sorted_coin[i] < total and sorted_coin[i] + new_total <= total:
            new_total += sorted_coin[i]
            number_of_coins += 1
        if new_total == total:
            return number_of_coins
            break

    if new_total != total:
        return -1
