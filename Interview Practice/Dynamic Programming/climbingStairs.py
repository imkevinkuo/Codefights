def climbingStairs(n): # 4 -> 5, 5 -> 8
    if n < 4:
        return n
    m = climbingStairs(n-1)
    # m does not include combinations where 2 steps last
    t = climbingStairs(n-2)
    return m+t
climbingStairs(5)
