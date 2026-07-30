class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        n = len(nums)
        res = []
        sort_nums = sorted(nums)
        def backtrack(idx, path):
            res.append(path.copy())
            if idx == n:
                return
            for i in range(idx, n):
                if i > idx and sort_nums[i - 1] == sort_nums[i]:
                    continue
                path.append(sort_nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res