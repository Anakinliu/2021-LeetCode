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
    s_len = len(s)
    if s_len == 1:
        return d[s[0]]
    pre = s[0]
    res = 0
    for v in s[1:]:
        if pre == 'I' and v == 'V':
            res += 4
        elif pre == 'I' and v == 'X':
            res += 9
        elif pre == 'X' and v == 'L':
            res += 40
        elif pre == 'X' and v == 'C':
            res += 90
        elif pre == 'C' and v == 'D':
            res += 400
        elif pre == 'C' and v == 'M':
            res += 900
        else:
            
        pre = v
