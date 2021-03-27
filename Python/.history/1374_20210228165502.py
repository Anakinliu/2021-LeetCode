def generateTheString(n):
    res = ''
    if n & 1:
        res += 'a' * n
    else:
        res = res + 'a'*(n-1) + 'b'
    return res

    