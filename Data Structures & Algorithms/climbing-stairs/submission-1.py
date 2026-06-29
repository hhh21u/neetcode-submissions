from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(None)
        def dp(count):
            if count == n:
                return 1
            if count > n:
                return 0
            # if cache[i] 
            return dp(count + 1) + dp(count + 2)
        return dp(0)
