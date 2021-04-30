# 二分法查找
def do(x):
    if x <= 1:
        print(x)
        return
    low = 1
    high = x // 2  # 引文一个整数的平方根必定小于等于 xx // 2
    mid = (low + high) // 2

    while low < high:
        if mid * mid == x:
            break
        if mid * mid < x:
            low = mid + 1
        if mid * mid > x:
            high = mid - 1
        mid = (low + high) // 2

    if mid * mid <= x:
        print(mid)
    else:
        print(mid - 1)

for i in range(20):
    print(i, end=' => ')
    do(i)