def twoSum(numbers, target):
    n = len(numbers)
    low = 0
    high = n - 1
    while numbers[low] + numbers[high] != target:
        s = numbers[low] + numbers[high]
        if s < target:
            low += 1
        if s > target:
            high -= 1
    return [low + 1, high + 1]


"""
[3,24,50,79,88,150,345] 
200
"""
print(twoSum([3,24,50,79,88,150,345], 200))