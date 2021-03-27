def numTrees(n):
    if n <= 2:
        return n
    dp_table = [0] * (n+1)
    dp_table[0] = 1
    dp_table[1] = 1
    for i in range(3, n+1):
        for j in range(0, i):
            dp_table[i] += dp_table[j] * dp_table[i-j-1]
    return dp_table[-1]

print(numTrees(5))
