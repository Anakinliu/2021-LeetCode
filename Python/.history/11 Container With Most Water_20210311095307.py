# 暴力解法,超时GG
def maxArea(height: List[int]) -> int:
    res = -1
    for i in range(len(height)):
        for j in range(i, len(height)):
            if height[j] <= height[i]:
                res = max(res, )
            else:
                res.append(height[i] * (j-i))
    return max(res)