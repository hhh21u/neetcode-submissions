class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_n = sum(nums)
        if sum_n % 2 != 0: 
            return False

        half = sum_n // 2
        n = len(nums)
        # memo = {}
        # def dfs(idx, remain):
        #     if (idx, remain) in memo:
        #         return memo[(idx, remain)]
        #     if remain == 0:
        #         return True
        #     if remain < 0 or idx >= n:
        #         return False
        #     memo[(idx, remain)] = dfs(idx + 1, remain) or dfs(idx + 1, remain - nums[idx])
        #     return memo[(idx, remain)]
        # return dfs(0, half)

        dp = [[False] * (half + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1 , n + 1):
            for j in range(1, half + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][half]




