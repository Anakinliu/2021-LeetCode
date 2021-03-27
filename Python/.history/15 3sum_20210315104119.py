def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    res = []
    print(sorted_nums)
    for p in range(nums_len-1):
        # print(sorted_nums[p])
        if sorted_nums[p] == sorted_nums[p+1]:
            continue
        right = nums_len - 1
        for left in range(0, nums_len-1):
            # print(sorted_nums[p],sorted_nums[left],sorted_nums[right])
            if sorted_nums[left] == sorted_nums[left+1]:
                continue
            if left <= right:
                print(sorted_nums[left])
                # 因为有 -4,0,0,1,1,2,2所以
                # if nums[right] == nums[right - 1]:
                #     right -= 1
                while sorted_nums[p] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                if left <= right and sorted_nums[p] + sorted_nums[left] + sorted_nums[right] == 0:
                    res.append([sorted_nums[p],sorted_nums[left],sorted_nums[right]])
                    continue
        print()
    print(res)


# -4,0,0,1,1,2,2,3,3
threeSum([-1,0,1,2,-1,-4])