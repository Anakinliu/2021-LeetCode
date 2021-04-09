# 想了俩小时没想到，原来就是进制转换。。。。
def titleToNumber(columnTitle):
    # ord('A') = 65
    res = 0
    for c in columnTitle:
        res = res * 26 + ord(c) - 64
    return res

# AB - 28
print(titleToNumber('ZY'))
