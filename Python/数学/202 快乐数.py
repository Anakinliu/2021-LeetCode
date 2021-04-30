# 保存已出现的数到集合里
def isHappy(n):
    def square_digit(n):
        return sum([int(v)**2 for v in str(n)])
    ap = set()
    while n not in ap:
        if n == 1:
            return True
        ap.add(n)
        n = square_digit(n)
    return False


# 快慢指针，快的计算两次两次计算，慢的一次计算一次
def isHappy2(n):
    def square_digit(n):
        return sum([int(v)**2 for v in str(n)])
    # if n == square_digit(n):
    #     return True
    slow = n
    fast = square_digit(square_digit(n))
    while slow != fast:
        slow = square_digit(slow)
        fast = square_digit(square_digit(fast))
    # print(slow, fast)
    if slow == 1:
        return True
    else:
        return False

print(isHappy(1))
"""
4 位或 4 位以上的数字在每一次 square_digit 都会丢失一位，直到降到 3 位为止。
所以我们知道，最坏的情况下，算法可能会在 243(9*9+9*9+9*9) 以下的所有数字上循环，
然后回到它已经到过的一个循环或者回到 1。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""