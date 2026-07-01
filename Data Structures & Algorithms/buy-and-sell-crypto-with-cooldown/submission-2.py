class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = {}  # key=(i, buying) val=max_profit

        # def dfs(i, buying):
        #     if i >= len(prices):
        #         return 0
        #     if (i, buying) in dp:
        #         return dp[(i, buying)]

        #     cooldown = dfs(i + 1, buying)
        #     if buying:
        #         buy = dfs(i + 1, not buying) - prices[i]
        #         dp[(i, buying)] = max(buy, cooldown)
        #     else:
        #         sell = dfs(i + 2, not buying) + prices[i]
        #         dp[(i, buying)] = max(sell, cooldown)
        #     return dp[(i, buying)]

        # return dfs(0, True)

        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                cooldown = dp[i + 1][buying]
                if buying:
                    buy = dp[i + 1][not buying] - prices[i]
                    dp[i][int(buying)] = max(buy, cooldown)
                else:
                    sell =dp[i + 2][not buying] + prices[i] if i + 2 < n else prices[i]
                    dp[i][int(buying)] = max(sell, cooldown)
        return dp[0][1]

                    



