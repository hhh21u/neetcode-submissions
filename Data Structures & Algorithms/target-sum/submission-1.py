class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # memo = {}
        # def dfs(idx, remain):
        #     if (idx, remain) in memo:
        #         return memo[(idx, remain)]
        #     if idx == n and remain == 0:
        #         return 1
        #     if idx >= n:
        #         return 0
        #     memo[(idx, remain)] = dfs(idx + 1, remain - nums[idx]) + dfs(idx + 1, remain + nums[idx])
        #     return memo[(idx, remain)]

        # return dfs(0, target)

        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]