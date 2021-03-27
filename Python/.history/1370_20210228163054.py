# 我的解答
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
##　@jamesujeon
def sortString2(s):
    s = list(s)
    result = ''
    while s:
        for letter in sorted(set(s)):
            s.remove(letter)
            result += letter
        for letter in sorted(set(s), reverse=True):
            s.remove(letter)
            result += letter
    return result

def sortString3(s):
    d = sorted([c, n] for c, n in collections.Counter(s).items())
    r = []
    while len(r) < len(s):
        for i in range(len(d)):
            if d[i][1]:
                r.append(d[i][0])
                d[i][1] -= 1
        for i in range(len(d)):
            if d[~i][1]:
                r.append(d[~i][0])
                d[~i][1] -= 1
    return ''.join(r)
s = "aaaabbbbcccc"
s = "rat"
s = "leetcode"
s = "ggggggg"
s = "spo"
print(sortString(s))
