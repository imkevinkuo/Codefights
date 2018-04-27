def answer(s):
    maxC = 1
    for i in range(1, int(len(s)/2)+1):
        if len(s)%i == 0:
            chunk = s[:i]
            broken = 0
            c = int(len(s)/i)
            for j in range(1, c):
                chunk2 = s[i*j:i*(j+1)]
                if chunk != chunk2:
                    broken = 1
                    break
            if not broken and c > maxC:
                maxC = c
    return maxC
a = answer("aaaaaa")
print(a)
