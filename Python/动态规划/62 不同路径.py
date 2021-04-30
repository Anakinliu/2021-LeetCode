# 一个二维数组，保存每个位置的路径数
def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])


# 代码优化,不需要保存所有的行，因为最多只用到了一行，再往前一行的状态就看不到了
def uniquePaths2(m, n):
    pre_line = [1]*n
    for _ in range(1, m):
        new_line = [1]
        for j in range(1, n):
            new_line.append(new_line[j-1] + pre_line[j])
        pre_line = new_line

    print(pre_line[-1])

# 再优化，其实只需要一个数组即可
def uniquePaths3(m, n):
    line = [1]*n
    for _ in range(1, m):
        for j in range(1, n):
            line[j] = line[j-1] + line[j]

    print(line[-1])


uniquePaths(70,70)
uniquePaths2(70,70)
uniquePaths3(70,70)
