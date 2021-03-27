# 单调栈
def nextGreaterElement(nums1, nums2):
    res = []
    stack = []
    for i in range(len(nums2)-1,-1,-1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        if not stack:
            res.insert(0, -1)
        else:
            res.insert(0, stack[-1])
        stack.append(nums2[i])
    # print(res)
    # res2 = []
    # for i in nums1:
    #     res2.append(res[nums2.index(i)])
    return [res[nums2.index(i)] for i in nums1]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))

nums1 = [2,4], nums2 = [1,2,3,4]