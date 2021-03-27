def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    res = []
    for p in range(nums_len):
        right = nums_len - 1
        for left in range(p+1, nums_len-1):
            print(sorted_nums[p],sorted_nums[left],sorted_nums[right])
            if left <= right:
                if sorted_nums[left] == sorted_nums[left + 1]:
                    continue
                # 因为有 -4,0,0,1,1,2,2所以
                # if nums[right] == nums[right - 1]:
                #     right -= 1
                if sorted_nums[p] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[p] + nums[left] + nums[right] == 0:
                    res.append([nums[p],nums[left],nums[right]])
                else:
                    continue
    print(res)


# -4,0,0,1,1,2,2,3,3
threeSum([-1,0,1,2,-1,-4])