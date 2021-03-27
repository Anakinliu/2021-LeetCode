def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    res = []
    for p in range(nums_len):
        right = nums_len - 1
        for left in range(p+1, nums_len):
            if left <= right:
                if nums[left] == nums[left + 1]:
                    continue
                # 因为有 -4,0,0,1,1,2,2所以
                # if nums[right] == nums[right - 1]:
                #     right -= 1
                if nums[p] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[p] + nums[left] + nums[right] == 0:
                    res.append([nums[p],nums[left],nums[right]])
                else:
                    continue
    print(res)


# -4,0,0,1,1,2,2,3,3
tr