def maxProfit(prices):
    n = len(prices)
    g = 0
    for i in range(n):
        for j in range(i,n):
            if prices[j] - prices[i] > g:
                g = max(g, prices[j] - prices[i])
    return g

print(maxProfit([7,1,5,3,6,4]))

def maxProfit2(prices):  # 遍历以便数组
    min_price = prices[0]
    max_income = 0
    for v in prices:
        if v < min_price


