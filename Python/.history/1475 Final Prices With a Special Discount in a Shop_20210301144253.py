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

#  @
p = [8,10,7,4,2,8,1,7,7,10,1]
print(finalPrices(p))