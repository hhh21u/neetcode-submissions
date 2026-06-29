class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n

        def dp(i):
            if i >= n: return 0
            if cache[i] != -1: return cache[i]
            cache[i] = min(dp(i + 1) + cost[i], dp(i + 2) + cost[i])
            return cache[i]

        return min(dp(0), dp(1))