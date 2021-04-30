"""
二分查找
"""

import math
def shipWithinDays(weights, D):
    # 确定二分查找左右边界
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        # need 为需要运送的天数
        # cur 为当前这一天已经运送的包裹重量之和
        need, cur = 1, 0
        for weight in weights:
            if cur + weight > mid:
                need += 1
                cur = 0
            cur += weight
        
        if need <= D:
            right = mid
        else:
            left = mid + 1
    
    return left



# weights = [3,2,2,4,1,4]
# D = 3
# 6

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
# 15
shipWithinDays(weights, D)