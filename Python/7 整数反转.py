def reverse(x):
    res = 0
    print(-(2**31), -1 + 2**31)
    print(x > -1 + 2**31)
    if x < -(2**31) or x > -1 + 2**31:
        return res
    if x <= 0:
        y = -x
    else:
        y = x
    while y:
        res = res * 10 + y % 10
        y = y // 10
    return res if x >= 0 else -res

print(reverse(1534236469))