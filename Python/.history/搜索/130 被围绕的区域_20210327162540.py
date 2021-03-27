def solve(board):
    """
    board[i][j] 为 'X' 或 'O'
    Do not return anything, modify board in-place instead.
    """
    # 不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'
    # =》与边界上的 'O' 相连的 'O' 最终都 不会被 填充为 'X'
    # ==》以边界上的 'O' 为起点，搜索！
    def dfs(i,j,table):
        stack = [(i,j)]
        # print(i,j)
        while stack:
            t = stack[-1]
            children = [(t[0]-1,t[1]),(t[0]+1,t[1]),(t[0],t[1]-1),(t[0],t[1]+1)]
            flag = True
            for child in children:
                x = child[0]
                y = child[1]
                if 0 < x < m and 0 < y < n and board[x][y] == 'O':
                    table[x][y] = True
                    stack.append((x,y))
                    flag = False
            if flag:
                stack.pop()
            
    m = len(board)
    n = len(board[0])
    table = [[False] * n for _ in range(m)]
    for i in range(m):  # i表示列下标
        for j in range(n):
            if board[i][j] == 'O' and (i in [0,m-1] or j in [0,n-1)):
                print(i,j)
                dfs(i,j,table)
    # print(table)


solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])