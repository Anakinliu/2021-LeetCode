def minPathSum(grid):
    """
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100
    """
    m = len(grid)
    n = len(grid[0])
    # dp_table = [[0] * n] * m  # 每一行都是同一个list，赋值会同时赋值。。。
    
    # dp_table[i][j]数组元素代表此位置的最小的路径和
    dp_table = [[0] * n for _ in range(m)]  
    dp_table[0][0] = grid[0][0]

    # 基准条件
    for i in range(1, n):  # 第一行只能一直向右走才能到达
        dp_table[0][i] = grid[0][i] + dp_table[0][i-1]
    for j in range(1,m):  # 第一列只能一直向下走才能到达
        dp_table[j][0] = grid[j][0] + dp_table[j-1][0]

    # 递进
    for i in range(1, m):
        for j in range(1, n):
            dp_table[i][j] = min(dp_table[i-1][j], dp_table[i][j-1]) + grid[i][j]
    return dp_table[-1][-1]