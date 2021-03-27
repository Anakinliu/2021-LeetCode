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
        'DM':900,
    }
    res = 0
    s_len = len(s)
    idx = 0
    while idx < s_len:
        if s[idx:idx+2] in d:
            res += d[s[idx:idx+2]]
            s += 2
    
print(romanToInt("IV"))
