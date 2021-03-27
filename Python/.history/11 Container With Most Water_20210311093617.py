# 暴力解法
def maxArea(height: List[int]) -> int:
    res = []
    for idx in range(len(height)):
        for j in range(idx, len(height))