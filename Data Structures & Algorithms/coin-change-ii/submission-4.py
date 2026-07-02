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
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[j] += dp[j - coins[i]]
        return dp[-1]

