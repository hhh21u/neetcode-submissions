class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curMax = 1
        curMin = 1
        res = nums[0]

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, num, curMin * num)
            curMin = min(tmp, curMin * num, num)
            res = max(curMax, res)
        return res
            
            