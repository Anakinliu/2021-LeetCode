# 最小数的左右两边的数都比它大
def findMin(nums):
    if nums[0] <= nums[-1]:
        return nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return nums[i]

# 比一般的二分多了两行
def findMin2(nums):
    if nums[0] <= nums[-1]:
        return nums[0]
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2

        # 比非旋转升序数组多了这两行
        if nums[mid] > nums[high]:
            low = mid + 1

        if nums[mid] < nums[high]:
            high = mid
    return min(nums[low], nums[high])  

print(findMin2([3,1]))