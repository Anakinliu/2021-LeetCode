def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # 先把nums1的数移到后面
    for i in range(m-1, m-n-1,-1):
        nums1[i] = nums1[i-n]
    print(nums1)
    a = n
    b = 0
    idx = 0
    while a < m+n and b < n:
        if nums1[a] < nums2[b]:
            nums1[idx] = nums1[a]
            a += 1
        else:
            nums1[idx] = nums2[b]
            b += 1
        idx += 1
    print(idx)
    while a < m+n:
        nums1[idx] = nums1[a]
        idx += 1
    while b < n:
        nums1[idx] = nums2[b]
        idx += 1
    print(nums1)

nums1 = [1,3,5,7,9,0,0,0]
nums2 = [2,4,6]
m = 8
n = 3
merge(nums1,m,nums2,n)