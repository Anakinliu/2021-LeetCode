def repeatedNTimes(A):
    # N+1个个不同元素，共2N个元素, 有一个元素重复了N次
    s = set()
    for v in A:
        if v in s:
            return v
        else:
            s.add(v)
    return -1

"""
A.length 是偶数 4 <= A.length <= 10000
# N+1个个不同元素，共2N个元素, 有一个元素重复了N次
则这个元素
1 2 1 4 1 6 1 8
[1,2,3,3]
[1,2,3,4,4,4]
[4,1,2,3,4,4]
前面的前面或者后面的后面有一个元素是其本身
"""
def repeatedNTimes2(A):
    for idx in range(0, len(A)-2):
        if A[idx+1] == A[idx] or A[idx+2] == A[idx]:
            return A[idx]
    return A[-1]
