# 暴力，超时
def maxProfit(prices):
    n = len(prices)
    g = 0
    for i in range(n):
        for j in range(i,n):
            if prices[j] - prices[i] > g:
                g = max(g, prices[j] - prices[i])
    return g

print(maxProfit([7,1,5,3,6,4]))

# 一次遍历
def maxProfit2(prices):  # 遍历以便数组
    min_price = prices[0]
    max_income = 0
    for v in prices[1:]:
        if v < min_price:
            min_price = v
        elif v - min_price > max_income:
            max_income = v - min_price
    return max_income

# 动态规划
def maxProfit3(prices):
    n = len(prices)
    if prices < 2:
        return 0
    dp_table = [[0] * 2 for _ in range(n)]

    dp_table[0][0] = 0
    dp_table[0][1] = -prices
    
    for v in prices[1:]:
        dp_table
