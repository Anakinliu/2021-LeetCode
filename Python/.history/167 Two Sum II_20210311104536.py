# 类似11-最大盛水, 不断减少搜索空间
def twoSum(numbers, target):
    left = 0
    right = len(target) - 1
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif:
