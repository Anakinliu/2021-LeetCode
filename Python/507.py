# 我的解答
def checkPerfectNumber(num):
    if num == 1:
        return False
    res = 1
    for n in range(2, int(num**0.5)+1): 
        if num % n == 0:
            res = res + n + num // n
##            print(n, ' ', num // n)
    return res == num

print(checkPerfectNumber(28))
print(checkPerfectNumber(6))  # True
print(checkPerfectNumber(1))
print(checkPerfectNumber(2))
print(checkPerfectNumber(3))
