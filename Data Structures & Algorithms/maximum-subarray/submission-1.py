class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = -float("inf")
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            res = max(res, curSum)
        return res