class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        cache = [[-1] * 2 for _ in range(n)]

        def dp(i, flag):
            if i >= n or (i == n - 1 and flag): return 0
            if cache[i][flag] != -1: 
                return cache[i][flag]
            cache[i][flag] = max(dp(i + 1, flag), dp(i + 2, (flag or i == 0)) + nums[i])
            return cache[i][flag]
        
        return max(dp(0, True), dp(1, False))