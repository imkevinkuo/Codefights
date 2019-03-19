def classifyStrings(s):
    # solution runs in O(n), unlike most other solutions which permute all possible classes of ?.
    vowels = set(['a','e','i','o','u'])
    n = 0
    v = 0
    qs = []
    ind = []
    # collect all candidate 'bad' substrings
    for i in range(len(s)):
        c = s[i]
        if c == '?':
            n += 1
            v += 1
        elif c in vowels:
            n = 0
            v += 1
        else:
            n += 1
            v = 0
        if n == 5:
            qs.append(s[i-4:i+1])
            ind.append(i-4)
        if v == 3:
            qs.append(s[i-2:i+1])
            ind.append(i-2)
    # a candidate bad substring with...
    # 0 ? is bad
    # 2+ is mixed
    # 1 ? is mixed or bad
    # when we have 1 ?, it is bad if the ? links two substring together and they are different classes.
    for i in range(len(qs)):
        q = qs[i]
        if '?' not in q:
            return "bad"
        elif i < len(qs)-1:
            if q.count('?') == 1:
                if q.index('?') == ind[i] + ind[i+1]:
                    if (q[0] in vowels) != (qs[i+1][-1] in vowels):
                        return "bad"
    if qs:
        return "mixed"
    return "good"
