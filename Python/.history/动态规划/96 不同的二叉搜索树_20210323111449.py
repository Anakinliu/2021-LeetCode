def numTrees(n):
    if n
    dp_table = [0] * n
    dp_table[0] = 1
    dp_table[1] = 2
    if n < 3:
        return dp_table[]
    for i in range(2, n):
        for j in range(0, i):
            dp_table[i] += dp_table[j] * dp_table[i-j-1]
    return dp_table[-1]

print(numTrees(3))
