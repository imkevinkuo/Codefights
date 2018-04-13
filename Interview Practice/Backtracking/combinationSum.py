def helper(arr, num, combos):
    finalSet = set()
    while combos:
        c = combos.pop()
        if sum(c) < num:
            for a in arr:
                if len(c) == 0 or a >= max(c):
                    combos.add(c + (a,))
            combos.discard(c)
        if sum(c) > num:
            combos.discard(c)
        if sum(c) == num:
            finalSet.add(c)
    return finalSet
def combinationSum(arr, num):
    combos = set()
    combos.add(tuple())
    combos = helper(arr, num, combos)
    if len(combos) == 0:
        return "Empty"
    s = ''.join("(" + ' '.join(str(d) for d in c) + ")" for c in sorted(combos))
    return s
