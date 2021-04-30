# 二维数组，保存第i天买入或卖出的所得
def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    dp_table = [[0] * 2 for _ in range(n)]

    dp_table[0][0] = 0
    dp_table[0][1] = -prices[0]

    for i in range(1,n):
        dp_table[i][0] = max(dp_table[i-1][0], prices[i] + dp_table[i-1][1])
        dp_table[i][1] = max(dp_table[i-1][1], -prices[i])
    # 返回最大收益
    return dp_table[-1][0]


#  只需迭代一次
def maxProfit2(prices):
    d = len(prices)
    max_pro = 0
    min_price = 100000
    for i in range(d):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_pro:
            max_pro = prices[i] - min_price
    return max_pro
            
