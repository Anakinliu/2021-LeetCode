# @101leetcode

def finalPrices(prices):
    ## RC ##
    ## APPROACH : STACK ##
    ## LOGIC ## 
    ## 1. Use Monotonic Increasing Stack Concept
    ## 2. Main idea is to find the Next Smaller Element in O(N) using #1
    stack = []
    for i, num in enumerate(prices):
        while(stack and prices[stack[-1]] >= num):
            popIndex = stack.pop()
            prices[popIndex] -= num
        stack.append(i)
    return prices

# 力扣@jasoncoding13
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and stack[-1][1] >= prices[i]:
                prices[stack[-1][0]] -= prices[i]
                stack.pop()
            stack.append((i, prices[i]))
        return prices

# 作者：jasoncoding13
# 链接：https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop/solution/pythondan-diao-zhan-on99on21shi-li-ti-ji-qv0y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

p = [8,10,7,4,2,8,1,7,7,10,1]
print(finalPrices(p))