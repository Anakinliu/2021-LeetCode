def missingNumber(nums):
    n = len(nums)
    s = (n * (n + 1)) // 2
    return s - sum(nums)

# print(missingNumber([0,1,3]))

# @Zrzr
def missingNumber2(nums):
    # 更好地防止溢出的写法
    s = 0
    for v in range(1,len(nums)+1):
        s += v
        s -= nums[v - 1]
    return s

print(missingNumber([0,1,3]))
