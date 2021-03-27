# 暴力解法
def maxArea(height: List[int]) -> int:
    res = []
    for i in range(len(height)):
        for j in range(i, len(height)):
            if height[j] <= height[i]:
                res.append(height[j] * (j-i))