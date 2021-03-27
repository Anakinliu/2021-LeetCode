def uniquePaths(m, n):
    dp_table = [[0]*n]*m
    dp_table[0] = [1] * n
    for i in range(m):
        dp_table[i][0] = 1
    for i in range(1, m):
        for j in range(1,n):
            dp_table[i][j] = dp_table[i-1][j] + dp_table[i][j-1]
    return dp_table[-1][-1]


print(uniquePaths(3,7))