def searchMatrix(matrix, target):
    m = len(matrix)  # 行
    n = len(matrix[0])  # 列
    i, j = 0, n-1
    while i < m and j < n:
