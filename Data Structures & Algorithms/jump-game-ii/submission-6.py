from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        # @lru_cache(True)
        # def dp(i):
        #     if i >= n - 1 or ((nums[i] + i) >= n - 1):
        #         return 1
        #     sub = n
        #     for j in range(i + 1, min(n, i + nums[i] + 1)):
        #         # print(f"{j}")
        #         sub = min(sub, dp(j))
        #     return 1 + sub

        # return dp(0)
        dp = [n for _ in range(n)]
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= n - 1:
                dp[i] = 1
                continue
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                dp[i] = min(dp[i], 1 + dp[j])
        print(dp)
        return dp[0]
