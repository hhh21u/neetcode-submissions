class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        # dp = [(amount + 1) for _ in range(amount + 1)]
        # dp[0] = 0
        
        # for i in range(1, amount + 1):
        #     for c in coins:
        #         if i - c >= 0:
        #             dp[i] = min(dp[i], 1 + dp[i - c])
        # return dp[-1] if dp[-1] != amount + 1 else -1

        cache = {}
        def dfs(remain):
            if remain == 0:
                return 0
            if remain in cache: return cache[remain]
            cache[remain] = float("inf")
            if remain < 0:
                return cache[remain]
            for c in coins:
                cache[remain] = min(cache[remain], 1 + dfs(remain - c))
            return cache[remain]
        res = dfs(amount)
        return -1 if res == float("inf") else res            
