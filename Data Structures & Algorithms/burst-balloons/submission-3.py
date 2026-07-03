class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        # dp = {}

        # def dfs(l, r):
        #     if l > r:
        #         return 0
        #     if (l, r) in dp: 
        #         return dp[(l, r)]
        #     dp[(l, r)] = 0
        #     for i in range(l, r + 1):
        #         cur = nums[l - 1] * nums[i] * nums[r + 1]
        #         cur += dfs(l, i - 1) + dfs(i + 1, r)
        #         dp[(l, r)] = max(dp[(l, r)], cur)
        #     return dp[(l, r)]

        # return dfs(1, len(nums) - 2)
        n = len(nums)
        dp = [[0] * (n) for _ in range(n) ]
        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                for mid in range(i, j + 1):
                    cur = nums[i - 1] * nums[mid] * nums[j + 1]
                    cur += dp[i][mid - 1] + dp[mid + 1][j]
                    dp[i][j] = max(cur, dp[i][j])
        return dp[1][n - 2]