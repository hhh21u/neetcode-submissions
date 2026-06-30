class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_n = sum(nums)
        if sum_n % 2 != 0: 
            return False

        half = sum_n // 2
        n = len(nums)
        memo = {}
        def dfs(idx, remain):
            if (idx, remain) in memo:
                return memo[(idx, remain)]
            if remain == 0:
                return True
            if remain < 0 or idx >= n:
                return False
            memo[(idx, remain)] = dfs(idx + 1, remain) or dfs(idx + 1, remain - nums[idx])
            return memo[(idx, remain)]

        return dfs(0, half)