def countNegatives(grid):
    res = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] < 0:
                res += (n - j)
                break
            pass
    return res

# @ikeabord 楼梯形状,负数是楼梯，从下网上爬
##    ++++++
##    ++++--
##    ++++--
##    +++---
##    +-----
##    +-----
def countNegatives2(grid):
    m = len(grid)
    n = len(grid[0])
    s = m - 1
    w = 0
    res = 0
    while s >= 0 and w < n:
        if grid[s][w] < 0:
            s -= 1
            res += (n - w)
        else:
            w += 1
    return res
            
