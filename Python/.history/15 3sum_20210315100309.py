def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    for p in range(nums_len):
        for right in range(p+1, nums_len):
            if nums[p]