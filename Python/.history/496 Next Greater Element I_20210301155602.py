# 单调栈
def nextGreaterElement(nums1, nums2):
    res = []
    stack = []
    for i in range(len(nums2)-1,-1):
        while not stack and stack[-1] <= nums2[i]:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(nums2[i])
    print(res)