def isPowerOfTwo(n):
    if n < 1:
        return False
    if n == 1:
        return True
    while n % 2 == 0:
        n = n >> 1
    if n == 1:
        return True
    else:
        return False


print(isPowerOfTwo(4))