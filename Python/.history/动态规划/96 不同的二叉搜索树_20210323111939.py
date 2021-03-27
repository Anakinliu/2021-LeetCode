def numTrees(n):
    if n < 3:
        return n
    dp_table = [0] * n
    dp_table[0] = 1
    dp_table[1] = 1
    dp_table[2] = 2
    for i in range(2, n):
        for j in range(0, i):
            print(j, i-j-1)
            dp_table[i] += dp_table[j] * dp_table[i-j-1]
    return dp_table[n-1]

print(numTrees(3))
