"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
# 贪心法
def maxSubArray(nums):
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in nums[1:]:
        if cur_sum >= 0:  # 此数之前的数的和
            cur_sum += i
            max_sum = max(max_sum, cur_sum)
        else:
            cur_sum = i
    return max_sum
    # print(max_sum)

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# 动态规划
# 如果前边累加后还不如自己本身大，那就把前边的都扔掉，从此自己本身重新开始累加
def maxSubArray2(nums):
    max_sum = nums[0]
    pre = 0
    for v in nums:
        pre = max(pre + v, v)
        max_sum = max(max_sum, pre)
    return max_sum