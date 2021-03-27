# 暴力解法,超时GG
def maxArea(height: List[int]) -> int:
    res = -1
    for i in range(len(height)):
        for j in range(i, len(height)):
            if height[j] <= height[i]:
                res = max(res, height[j] * (j-i))
            else:
                res = max(res, height[i] * (j-i))
    return res

#  