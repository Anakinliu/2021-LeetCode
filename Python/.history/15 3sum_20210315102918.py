def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    res = []
    print(sorted_nums)
    for p in range(nums_len):
        print(sorted_nums[p])
        right = nums_len - 1
        for left in range(p+1, nums_len-1):
            # print(sorted_nums[p],sorted_nums[left],sorted_nums[right])
            if left <= right:
                if sorted_nums[left] == sorted_nums[left + 1]:
                    continue
                # 因为有 -4,0,0,1,1,2,2所以
                # if nums[right] == nums[right - 1]:
                #     right -= 1
                while sorted_nums[p] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                if left <= right and sorted_nums[p] + sorted_nums[left] + sorted_nums[right] == 0:
                    res.append([sorted_nums[p],sorted_nums[left],sorted_nums[right]])
                    continue
    print(res)


# -4,0,0,1,1,2,2,3,3
threeSum([-1,0,1,2,-1,-4])