def bubbleSort(arr):
    arr_len = len(arr)

    for i in range(0,arr_len-1):
        for j in range(0, arr_len-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [1,4,5,7,2,4,6,8]
print(bubbleSort(arr))