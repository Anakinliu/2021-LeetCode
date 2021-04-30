# 我把等于val的值全部移到数组后面
def removeElement(nums, val):
    n = len(nums)
    if n == 0:
        return 0
    idx = 1
    count = 0

    # 从后到前将 idx 移到值不是 val 的位置
    for i in range(n):
        if nums[i] == val:
            # print(i, -idx)
            while idx <= n and nums[-idx] == val:
                count += 1
                idx += 1
            if i < n - idx:
                # print(i, -idx)
                nums[-idx], nums[i] = nums[i], nums[-idx]
            else:
                # print('break ', idx)
                break
    # print('共：', count, '新长度 ', n - count)
    return n - count 

# 我的改版，去掉不必要的 swap 操作
def removeElement2(nums, val):
    n = len(nums)
    if n == 0:
        return 0
    idx = 1
    count = 0

    # 从后到前将 idx 移到值不是 val 的位置
    for i in range(n):
        if nums[i] == val:
            while idx <= n and nums[-idx] == val:  # 上次交换后的的idx位置的值为val，这次正好在count加上
                count += 1
                idx += 1
            if i < n - idx:
                nums[i] = nums[-idx]  # 不必交换，应为题目不需要那些值了
                count += 1
                idx += 1
            else:
                break
            
    return n - count 

# 官解一，直接覆盖等于 val 的值。不需要交换操作。
def removeElement1(nums, val):
    n = len(nums)
    slow = 0
    fast = 0
    for _ in range(n):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow
# 官解二
def removeElement3(nums, val):
    n = len(nums)
    left = 0
    right = n-1
    while left < right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -=1
        else:
            left += 1
    return left


nums = [0,1,2,2,3,0,4,2]
val = 2
print('res ', nums[:removeElement(nums, val)])
print()
nums = [2]
val = 2  # 
print('res ', nums[:removeElement(nums, val)])
print()
nums = [2]
val = 3
print('res ', nums[:removeElement(nums, val)])
print()
nums = [0,4,4,0,4,4,4,0,2]
val = 4  # 4, [0,2,0,0]
print('res ', nums[:removeElement(nums, val)])
