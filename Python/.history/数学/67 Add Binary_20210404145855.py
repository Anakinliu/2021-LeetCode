"""
a,b是二进制，字符串，返回a+b的结果，二进制表示。
"""
def addBinary(a,b):
    a_len = len(a)
    b_len = len(b)
    i = -1
    i_sum = 0    
    while i >= -a_len and i <= -b_len:
        
