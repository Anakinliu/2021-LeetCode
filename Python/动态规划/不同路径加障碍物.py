# 一个二维数组，保存每个位置的路径数
grid = [[0,0,0,0,0,1,0],
        [0,0,0,1,0,0,0],
        [0,1,0,0,0,0,0]]

def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if dp[i][0] == 1:
            break  # 后面的就不可达了
        dp[i][0] = 1
    for i in range(n):
        if grid[0][i] == 1:
            break  # 后面的就不可达了
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])

uniquePaths(3,7)

# 优化同 62.不同路径，只是判断有无障碍物，设置为0即可

