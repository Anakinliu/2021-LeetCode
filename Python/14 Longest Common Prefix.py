# 最长公共前缀，时间O(N*M)
# strs = ["flower","flow","flight"]
def longestCommonPrefix(strs):
    if not strs:
        return ""
    s_len = len(strs)
    point = strs[0]  # 以第一个为标准
    for s in strs[1:]:
        idx = 0  # # 开始查看一个字符串，初始化最长公共长度为0
        for a,b in zip(s, point):
            if a == b:
                idx += 1
            else:
                break
        point = point[:idx]  # 每走完一个字符串，更新最长公共长度

    return point

# @SimplyFaisal
def longestCommonPrefix2(strs):
    """
    时间：O(N*M)有剪枝的
    """
    if not strs:
        return ""
    shortest = min(strs,key=len)  # 先按照字符串长度升序排列
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 

# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["flower","flow"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["dog"]))
# print(longestCommonPrefix(["dog","racecar"]))
# print(longestCommonPrefix(["ca","c","bba","bacb","bcb"]))
# print(longestCommonPrefix2(["aaab","acbd","aaa"]))
