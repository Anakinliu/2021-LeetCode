def diStringMatch(S):
    # 1 <= S.length <= 10000
    # A包含[0, 1, ..., N]，每个数只出现一次, A可能不唯一
    # 解法：每次I 都选择剩余数里最小的，每次D都选择最大的
    res = []
    increase = 0
    decrease = len(S)
    for i in S:
        if i == "I":
            res.append(increase)
            increase += 1
        else:
            res.append(decrease)
            decrease -= 1
    # print(decrease, increase)
    res.append(increase)
    return res


# @lee215 Inside-out and subtract left:
def diStringMatch2(S):
    left = right = 0
    res = [0]
    for i in S:
        if i == "I":
            right += 1
            res.append(right)
        else:
            left -= 1
            res.append(left)
    print(res)
    # return [i - left for i in res]
    return [i - left for i in res]


print(diStringMatch("IDID"))
# print(diStringMatch2("IDID"))
# print(diStringMatch("DDI"))
