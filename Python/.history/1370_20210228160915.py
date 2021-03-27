
def sortString(s):
    # s contains only lower-case English letters.
    res = []   
##    s_lst = list(s)
    s_dct = dict()
    for c in s:
        if c not in s_dct.keys():
            s_dct[c] = 1
        else:
            s_dct[c] += 1
##    print(s_dct.values())
    s_lst = sorted(list(set(s)))
    while any(s_dct.values()):
        for c in s_lst:
            if s_dct[c] > 0:
                res.append(c)
                s_dct[c] -= 1
        for c in reversed(s_lst):
            if s_dct[c] > 0:
                res.append(c)
                s_dct[c] -= 1
                
##    print(res) 
    return "".join(res)
s = "aaaabbbbcccc"
s = "rat"
s = "leetcode"
s = "ggggggg"
s = "spo"
print(sortString(s))
