# 常规解法
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # 先把nums1的数移到后面
    for i in range(m-1, n-1,-1):
        nums1[i] = nums1[i-n]
    print(nums1)
    a = n
    b = 0
    idx = 0
    while a < m and b < n:
        if nums1[a] < nums2[b]:
            nums1[idx] = nums1[a]
            a += 1
        else:
            nums1[idx] = nums2[b]
            b += 1
        idx += 1
    while a < m:
        nums1[idx] = nums1[a]
        idx += 1
        a += 1
    while b < n:
        nums1[idx] = nums2[b]
        idx += 1
        b += 1
    print(nums1)


def merge2(nums1, m, nums2, n):    
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1  # nums1尾索引
    p2 = n - 1  # nums2尾索引
    p = m + n - 1  # 合并后的尾索引
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p], nums1[p1] = nums1[p1], nums1[p]
            p1 -= 1
        p -= 1
    print(p1, p2)
    # 若p1>=
    nums1[:p2 + 1] = nums2[:p2 + 1]  # p2大于等于0

nums1 = [1,3,5,7,9, 0, 0, 0]
nums2 = [2,4,6]
m = 5
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
merge2(nums1,m,nums2,n)