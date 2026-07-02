class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()

        cache = {}
        def dfs(idx, remain):
            if (idx, remain) in cache:
                return cache[(idx, remain)]
            if remain == 0:
                return 1
            if idx >= n or remain < 0:
                return 0
            cache[(idx, remain)] = 0
            if coins[idx] <= remain:
                cache[(idx, remain)] = dfs(idx + 1, remain)
                cache[(idx, remain)] += dfs(idx, remain - coins[idx])
            return cache[(idx, remain)]

        return dfs(0, amount)

