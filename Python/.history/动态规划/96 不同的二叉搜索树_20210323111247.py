def numTrees(n):
    dp_table = [0] * n
    dp_table[0] = 1
    dp_table[1] = 2
    if n < 3:
        return dp_table[n-1]
    for i in range(2, n):
        for j in range(0, i):
            dp_table[i] += dp_table
