# 暴力解法,超时GG
def maxArea(height):
    res = -1
    for i in range(len(height)):
        for j in range(i, len(height)):
            if height[j] <= height[i]:
                res = max(res, height[j] * (j-i))
            else:
                res = max(res, height[i] * (j-i))
    return res

# 双指针，leetcode-cn官方题解
def maxArea(height):
    left = 0
    right = height - 1
    res = -1
    while