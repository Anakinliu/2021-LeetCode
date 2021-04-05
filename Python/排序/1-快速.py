def partition(arr, low, high):
    i = low - 1  # 最小是-1，即最后一个元素
    p = arr[high]  # 选取当前分区[left, rifht]的最高位为p
    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick(arr, left, right):
    if len(arr) == 1:
        return arr
    if left < right:
        p = partition(arr, left, right)
        quick(arr, left, p-1)
        quick(arr, p + 1, right)

arr = [8,1,3,5,7,2,4,6,8]
quick(arr, 0, len(arr)-1)
print(arr)