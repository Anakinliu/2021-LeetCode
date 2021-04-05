def insert_sort(arr):
    for idx in range(1, len(arr)):
        # 从idx处向前扫描，寻找插入位置

        pre = idx - 1
        cur = arr[idx]  # 保存arr[idx]值
        while pre >= 0 and arr[pre] > cur:  # 这里保证了是稳定的，会终止循环。
            arr[pre+1] = arr[pre] 
            pre -= 1
        arr[pre+1] = cur  # 此时pre位置的数雄鱼cur，故将cur+1位置替换为cur


arr = [1,3,5,7,9,2,4,6,8]
insert_sort(arr)
print(arr)