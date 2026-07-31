class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        paths = []

        def backtrack(idx, path):
            paths.append(path.copy())
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(0, [])
        return paths