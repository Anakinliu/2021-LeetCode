def minimumTotal(triangle):
    """
    1
    23
    456
    ....
    """
    m = len(triangle)
    n = len(triangle[0])
    # dp_table[i][j] 为此位置的最小的路径的和
    dp_table = [[0] *  for _ in range(m)]
    dp_table[0][0] = triangle[0][0]
    for i in range(1, m):  # 第一”列“与最右”列“初始化,他们只能由上面一层的相同列得到
        dp_table[i][0] = dp_table[i-1][0] + triangle[i][0]
        print(i, i-1)
        dp_table[i][i] = dp_table[i-1][i-1] + triangle[i][i]
        
        for j in range(1, i):
            dp_table[i][j] = min(dp_table[i-1][j], dp_table[i-1][j-1])
    return min(dp_table[-1])


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))