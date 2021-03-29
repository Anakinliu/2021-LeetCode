"""
第一次自己写的双99%的题解。。。
"""
def countBits(num):
    # 0 0000
    # 1 0001 1
    # 2 0010 1
    # 3 0011 2
    # 4 0100 1
    # 5 0101 2
    # 6 0110 2
    # 7 0111 3
    # 8 1000 1
    # 9 1001 2
    #10 1010 2
    #11 1011 3
    lst = [0] * (num+1)
    for i in range(1, num+1):
        if i % 2: # 奇数
            lst[i] = lst[(i-1) // 2] + 1
        else:
            lst[i] = lst[i // 2]
    return lst

"""
输入: 5
输出: [0,1,1,2,1,2]
"""
print(countBits(2))
