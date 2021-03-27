def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    for i in range(n):
        g = 0
        for j in range(i,n):
            if prices[j] - prices[i] > g:
                g = max(g, prices[j] - prices[i])
    return g