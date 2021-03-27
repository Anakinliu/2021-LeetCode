def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    for p in range(nums_len):
        for right in range(p+1, nums_len):
            while nums[right] != nums[right + 1

-3,0,0,1,1,2,2