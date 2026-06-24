class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2, 

        nums.sort()
        res = set()

        def twoSum(nums, target):
            left, right = 0, len(nums) - 1
            res = []
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                if nums[left] + nums[right] > target: 
                    right -= 1
                else:
                    left += 1
            return res

        for i in range(len(nums) - 1):
            if nums[i] > 0: break
            subs = twoSum(nums[i + 1:], -nums[i])
            if len(subs) == 0: continue
            for sub in subs:
                three = (nums[i], sub[0], sub[1])
                res.add(three)
        return list(res)