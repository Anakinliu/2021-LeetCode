"""
输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。

 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
"""
# 你可以不使用循环或者递归，
# 且在 O(1) 时间复杂度内解决这个问题吗？

# @恒等式
def addDigits(num):
    """
    能够被9整除的整数，各位上的数字加起来也必然能被9整除，所以，连续累加起来，最终必然就是9。
不能被9整除的整数，各位上的数字加起来，结果对9取模，和初始数对9取摸，是一样的，所以，连续累加起来，最终必然就是初始数对9取摸。
    """
    if 0 == num % 9:
        return 9
    return num % 9;


for i in range(50):
    print(addDigits(i))













