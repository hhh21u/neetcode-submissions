from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [n for _ in range(n)]
        # dp[n - 1] = 1
        # for i in range(n - 2, -1, -1):
        #     if nums[i] + i >= n - 1:
        #         dp[i] = 1
        #         continue
        #     for j in range(i + 1, min(n, i + nums[i] + 1)):
        #         dp[i] = min(dp[i], 1 + dp[j])
        # print(dp)
        # return dp[0]
        
        # breadth first search
        l = r = 0
        res = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            res += 1
        return res
        