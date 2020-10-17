

def coin_change(coins, value):
    amount = 0
    change = []
    coins = sorted(coins)
    while value != 0:
        for coin in reversed(coins):
            if coin <= value:
                change.append(coin)
                amount += 1
                value -= coin
                break
    print(change)
    return amount


def coin_change_dp(coins, value):
    changes = [value] * (value+1)
    changes[0] = 0
    for coin in coins:
        for x in range(coin, value+1):
            changes[x] = min(changes[x], changes[x - coin] + 1)
    return changes[value]


print(coin_change_dp([1, 6, 13], 31))

coin_change([1, 6, 13], 31)

# Simple Subproblems
# Subproblems optimization
# Subproblem overlap

# [13, 13, 1, 1, 1, 1, 1]
