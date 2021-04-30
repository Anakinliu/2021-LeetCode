# 先判断旋转的次数是否超过了数组长度的一半
def findMin2(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        elif nums[mid] < nums[high]:
            high = mid
        # 与153 题相比，多了这一行，即不能确定最小值在mid的左边还是右边，但是可以确定在high的左边。。。
        else:
            high -= 1
        

    return min(nums[low], nums[high])  



