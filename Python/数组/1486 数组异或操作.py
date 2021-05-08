def xorOperation(n, start):
    res = start
    for i in range(1, n):
        res = res ^ (start + 2 * i)
    return res

print(xorOperation(4, 3))
print(xorOperation(1, 7))
print(xorOperation(10, 5))

