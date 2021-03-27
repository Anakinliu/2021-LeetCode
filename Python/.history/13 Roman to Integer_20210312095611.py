def romanToInt(s):
    d = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900,
    }
    res = 0
    s_len = len(s)
    idx = 0
    while idx < s_len:
        if s[idx:idx+2] in d:
            res += d[s[idx:idx+2]]
            idx += 2
        else:
            res += d[s[idx]]
            idx += 1
        print(res)
    return res


# 小值在左则减
def romanToInt(s):
    d = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    res = 0
    s_len = len(s)
    idx = 0
    pre = 0
    while idx < s_len:
        if s[pre] < s[idx]:
            res -= 2 * s[pre]
        else:
            res += s[idx]
        pre = idx
        idx += 1
    return res
    
print(romanToInt("MCMXCIV"))
