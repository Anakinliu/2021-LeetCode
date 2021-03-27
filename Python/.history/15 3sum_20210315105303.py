def threeSum(nums):
    sorted_nums = sorted(nums)
    nums_len = len(nums)
    res = []
    print(sorted_nums)
    for p in range(nums_len-1):
        # print(sorted_nums[p])
        right = nums_len - 1
        if p >= 1 and sorted_nums[p] == sorted_nums[p-1]:
            continue
        print(p)
        for left in range(p+1, nums_len-1):
            # print(sorted_nums[p],sorted_nums[left],sorted_nums[right])
            if left >= p + 2 and sorted_nums[left] == 
            if left <= right:
                # print(sorted_nums[left])
                # 因为有 -4,0,0,1,1,2,2所以
                # if nums[right] == nums[right - 1]:
                #     right -= 1
                while sorted_nums[p] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                if left <= right and sorted_nums[p] + sorted_nums[left] + sorted_nums[right] == 0:
                    res.append([sorted_nums[p],sorted_nums[left],sorted_nums[right]])
                    continue
        print()
    print('res=',res)


# -4,0,0,1,1,2,2,3,3
# threeSum([-1,0,1,2,-1,-4])
threeSum([0,0,0,0,0,0])