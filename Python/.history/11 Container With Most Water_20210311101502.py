# 暴力解法,超时GG,时间O(N^2)，空间O（1）
def maxArea(height):
    res = -1
    for i in range(len(height)):
        for j in range(i, len(height)):
            if height[j] <= height[i]:
                res = max(res, height[j] * (j-i))
            else:
                res = max(res, height[i] * (j-i))
    return res

# 双指针，leetcode-cn官方题解，时间O(N),空间O（1）
def maxArea2(height):
    left = 0
    right = height - 1
    res = -1
    while left < right:
        res = max(res, min(height[left], height[height]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res
