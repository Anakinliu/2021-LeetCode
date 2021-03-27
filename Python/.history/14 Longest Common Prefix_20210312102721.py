# 最长公共前缀
def longestCommonPrefix(strs):
    s_len = len(strs)

    if s_len == 0:
        return ""
    if s_len == 1:
        return strs[0]

    longest = ""
    idx = 1
    while idx < s_len:
        if strs[idx].startswith(longest):
            print('in')
            cur = strs[idx]
            pre = strs[idx-1]
            print(cur,pre)
            for i,(a,b) in enumerate(zip(cur, pre)):
                print(i,a,b)
                if a != b:
                    print(i)
                    break
            longest = cur[:i]
        else:
            break
        idx += 1
    return longest

# print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["flower","flow"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["dog"]))
# print(longestCommonPrefix(["dog","racecar"]))
