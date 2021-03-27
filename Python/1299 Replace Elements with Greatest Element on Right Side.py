"""
将元素用它右边的最大元素替换
"""
# 暴力,时间O(N^2),空间O(1)
def replaceElements(arr):
    # if len(arr) == 1:
    #     return [-1]
    for i in range(len(arr)):
        if arr[i+1:]:
            arr[i] = max(arr[i+1:])
    arr[-1] = -1
    print(arr)


# arr = [17,18,5,4,6,9,8,7,10,12,11,1]
arr = [17,18,5,4,6,1]
# arr = [17,]


# @lee215,时间O(N),空间O(1)
def replaceElements2(arr):
    mx = -1
    for i in range(len(arr)):
        t = arr[~i]
        arr[~i] = mx
        mx = max(mx, t)
        # 或者one line 
        # mx, arr[~i] = max(arr[~i], mx), mx

replaceElements2(arr)
print(arr)
