def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    for p in range(nums_len):
        right = nums_len - 1
        for left in range(p+1, nums_len):
            if nums[left] == nums[left + 1] and nums[right] != nums[right - 1]:


-3,0,0,1,1,2,2