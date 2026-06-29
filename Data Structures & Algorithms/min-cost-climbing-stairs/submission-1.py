class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # cache = [-1] * n

        # def dp(i):
        #     if i >= n: return 0
        #     if cache[i] != -1: return cache[i]
        #     cache[i] = min(dp(i + 1) + cost[i], dp(i + 2) + cost[i])
        #     return cache[i]

        # return min(dp(0), dp(1))

        dp = [0] * (n + 1)

        # dp[0], dp[1] = 0, 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


