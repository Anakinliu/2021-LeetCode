# 二分法查找
def mySqrt(x):
    if x <= 1:
        return x
    low, high = 0, x
    mid = (high - low) // 2
    res = mid * mid
    while low < high and res != x:
        res = mid * mid
        if res < x:
            low = mid + 1  # 要加一，不然当low与high之间只有零个/一个元素时，会死循环
            mid = (high + low) // 2
        elif res > x:
            high = mid - 1
            mid = (high + low) // 2
        else:
            break
    return mid if mid * mid <= x else mid -1

for i in range(20):
    print(i, '-', mySqrt(i))