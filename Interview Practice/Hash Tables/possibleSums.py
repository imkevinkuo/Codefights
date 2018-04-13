def possibleSums(coins, quantity):
    newCoins = {}
    for i in range(len(coins)):
        if coins[i] not in newCoins:
            newCoins[coins[i]] = quantity[i]
        else:
            newCoins[coins[i]] += quantity[i]
    valids = set()
    valids.add(0)
    # fill in all multiples of biggest value
    # fill in gaps with smaller values
    while len(newCoins) > 0:
        tempValids = set(v for v in valids)
        m = max(newCoins)
        for i in range(0, newCoins[m]+1):
            for t in tempValids:
                valids.add(t + i*m)
        del newCoins[m]
    if 0 in valids:
        valids.remove(0)
    return len(valids)
