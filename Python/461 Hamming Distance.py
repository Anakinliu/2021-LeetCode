# 异或后 1 的个数
def hammingDistance(x, y):
    z = x ^ y
    return bin(z).count('1')
