class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(idx, prev):
            if (idx, prev) in memo: return memo[(idx, prev)]
            if idx >= n: 
                return 0
            memo[(idx, prev)] = dfs(idx + 1, prev)
            if nums[idx] > prev:
                memo[(idx, prev)] = max(memo[(idx, prev)], 1 + dfs(idx + 1, nums[idx]))
            return memo[(idx, prev)]

        # dfs(0, -float("inf"))
        # print(memo)

        return dfs(0, -float("inf"))