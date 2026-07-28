class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] > nums[r]:
                l = mid 
            else:
                r = mid - 1
            res = min(res, nums[mid])
        return res
