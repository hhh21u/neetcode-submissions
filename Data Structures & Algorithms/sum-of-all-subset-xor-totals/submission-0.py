class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = [0]
        
        def bt(idx, res):
            if idx == len(nums):
                return
            new = res ^ nums[idx]
            total[0] += new
            bt(idx + 1, res)
            bt(idx + 1, new)
        
        bt(0, 0)
        return total[0]