class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        # visited = set()
        def dfs(idx, total):
            if total == target:
                # visited.add(tuple(subset))
                res.append(subset.copy())
            if idx >= len(nums) or total >= target:
                return
            subset.append(nums[idx])
            dfs(idx, total + nums[idx])
            subset.pop()
            dfs(idx + 1, total)
        dfs(0, 0)
        return res