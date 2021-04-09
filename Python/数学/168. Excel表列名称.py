def convertToTitle(columnNumber):
    n = columnNumber
    res = []
    while n > 0:
        n -= 1
        res.append(chr(65 + n % 26))
        n = n // 26
    return ''.join(list(reversed(res)))

def convertToTitle2(columnNumber):
    n = columnNumber
    res = []
    while n > 0:
        res.append(chr(64 + n % 26) if n % 26 else 'Z')
        n = (n - 1) // 26
    return ''.join(list(reversed(res)))

# convertToTitle(26)
# convertToTitle(702)
# convertToTitle(703)
for i in range(7000, 7002):
    print(convertToTitle(i))
for i in range(52, 55):
    print(convertToTitle2(i))