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
    for k,v in d.items():
        s.count(k)
    
print(romanToInt("IV"))
