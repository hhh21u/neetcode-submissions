class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dfs(idx, buyIdx):
            if (idx, buyIdx) in memo: 
                return memo[(idx, buyIdx)]
            if idx >= n:
                return 0
            memo[(idx, buyIdx)] = 0
            if buyIdx == -1:
                # we can either buy or skip this day
                memo[(idx, buyIdx)] = max(dfs(idx + 1, idx) - prices[idx], dfs(idx + 1, buyIdx))
            else:
                # we can either sell or skip this day
                memo[(idx, buyIdx)] = max(prices[idx] + dfs(idx + 2, -1), dfs(idx + 1, buyIdx))
            return memo[(idx, buyIdx)]

        return dfs(0, -1)