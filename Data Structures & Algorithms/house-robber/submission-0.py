class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        cache = [-1] * n
        def dp(i):
            if i >= n: return 0
            if cache[i] != -1: return cache[i]
            cache[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return cache[i]
        return dp(0)