class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()

        # cache = {}
        # def dfs(idx, remain):
        #     if (idx, remain) in cache:
        #         return cache[(idx, remain)]
        #     if remain == 0:
        #         return 1
        #     if idx >= n or remain < 0:
        #         return 0
        #     cache[(idx, remain)] = 0
        #     if coins[idx] <= remain:
        #         cache[(idx, remain)] = dfs(idx + 1, remain)
        #         cache[(idx, remain)] += dfs(idx, remain - coins[idx])
        #     return cache[(idx, remain)]

        # return dfs(0, amount)

        # bottom up
        dp = [[0] * (n + 1) for _ in range(amount + 1)]
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(1, amount + 1):
            for j in range(n - 1, -1, -1):
                if coins[j] <= i:
                    dp[i][j] = dp[i][j + 1] + dp[i - coins[j]][j]
        return dp[amount][0]

