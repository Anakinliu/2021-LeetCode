def maxProfit(prices):
    n = len(prices)
    for i in range(n):
        g = 0
        for j in range(i,n):
            if prices[j] - prices[i] > g:
                g = max(g, prices[j] - prices[i])
    return g

print(maxProfit([7,1,5,3,6,4]))