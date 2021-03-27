def searchMatrix(matrix, target):
    m = len(matrix)  # 行
    n = len(matrix[0])  # 列
    i, j = 0, n-1
    while 0 <= i < m and 0 <= j < n:
        if matrix[i][j] < target:
            i += 1
        elif matrix