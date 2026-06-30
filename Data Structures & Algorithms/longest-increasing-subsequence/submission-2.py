class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = {}
        # def dfs(idx, prev):
        #     if (idx, prev) in memo: return memo[(idx, prev)]
        #     if idx >= n: 
        #         return 0
        #     memo[(idx, prev)] = dfs(idx + 1, prev)
        #     if nums[idx] > prev:
        #         memo[(idx, prev)] = max(memo[(idx, prev)], 1 + dfs(idx + 1, nums[idx]))
        #     return memo[(idx, prev)]
        # return dfs(0, -float("inf"))

        dp = [0] * (n + 1)
        res = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if j == n or nums[j] > nums[i]:
                    # print(f"p: {dp}")
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(res, dp[i])
        return res


