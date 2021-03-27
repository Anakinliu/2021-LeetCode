# dp_table 记忆 i 下表为结束的最长递增子序列长度
def lengthOfLIS(nums):
    n = len(nums)
    if n == 1:
        return 1
    # 第 i 个数时的最长递增子序列
    dp_table = [0] * n
    dp_table[0] = 1
    for i in range(1, n):
        max_len = 0
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i] and dp_table[j] > max_len:
                max_len = dp_table[j]
        dp_table[i] = max_len
    return max(dp_table)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))