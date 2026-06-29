from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:

        # @lru_cache(None)
        cache = [-1] * n
        def dp(count):
            if count == n:
                return 1
            if count > n:
                return 0
            if cache[count] != -1:
                return cache[count]
            cache[count] = dp(count + 1) + dp(count + 2)
            return cache[count]
        return dp(0)
