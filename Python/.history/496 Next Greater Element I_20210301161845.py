# 参考单调栈
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
    return [res[nums2.index(i)] for i in nums1]

# @harshkothari410
def nextGreaterElement2(nums1, nums2):
    d = {}
    st = []
    ans = []
    # st [1]
    # d{ 1:3 } st [3]
    # d{ 1:3 , 3:4 } st [4]
    # d{ 1:3 , 3:4 } st [4,2]
    # d{ 1:3 , 3:4 } st [4,2] => d{ 1:3 , 3:4 , 2:5 } st [4] => d{ 1:3 , 3:4 , 2:5 , 4:5 } st []
    for x in nums2:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)

    for x in nums1:
        ans.append(d.get(x, -1))
        
    return ans

nums1 = [4,1,2]
nums2 = [1,3,4,2,5]
print(nextGreaterElement(nums1, nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))
