def numTrees(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp_table = [0] * n
    dp_table[0] = 1
    dp_table[1] = 2
    for i in range(2, n):
        for j in range(0, i):
            dp_table[i] += dp_table[j] * dp_table[i-j-1]
    return dp_table[n-1]

print(numTrees(3))
