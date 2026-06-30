class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        suffix = 0
        res = nums[0]
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - i - 1] * (suffix or 1)
            res = max(max(prefix, suffix), res)
        return res
            
            