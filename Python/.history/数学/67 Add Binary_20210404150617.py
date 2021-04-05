"""
a,b是二进制，字符串，返回a+b的结果，二进制表示。
"""
def addBinary(a,b):
    a_len = len(a)
    b_len = len(b)
    i = -1   
    pre_sum = 0
    res = []
    while i >= -a_len and i <= -b_len:
        i_sum = int(a[i]) + int(b[i]) + pre_sum
        res.append(i_sum % 2)
        if i_sum > 1:
            pre_sum = 1
