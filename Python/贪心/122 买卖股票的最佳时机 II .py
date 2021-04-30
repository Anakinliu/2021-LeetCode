# 你可以尽可能地完成更多的交易,
# 你必须在再次购买前出售掉之前的股票
def maxProfit(prices):
    """
    定义状态 dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，
    dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）。

    """
    d = len(prices)
    t = [[0] * 2 for _ in range(d)]
    # 0 不持有时的收益， 1 持有时的收益
    t[0][0] = 0
    t[0][1] = -prices[0]
    for i in range(1, d):
        # 取决于昨天，昨天又分为持有和不持有

        # 昨天持有，今天不持有，就是今天抛出
        # 昨天不持有，今天不持有，就是昨天不持有时的收益
        t[i][0] = max(prices[i] + t[i-1][1], t[i-1][0])

        # 昨天持有，今天持有
        t[i][1] = max(t[i-1][1], t[i-1][0] - prices)
    # 最后一天不持有股票收益一定大于持有股票
    return t[-1][0]
