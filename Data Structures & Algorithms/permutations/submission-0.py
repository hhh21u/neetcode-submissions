class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        count = Counter(nums)
        paths = []
        
        def backtrace(idx, path):
            if idx == len(nums):
                paths.append(path)
                return
            for c, i in count.items():
                if i == 0:
                    continue
                count[c] -= 1
                backtrace(idx + 1, path + [c])
                count[c] += 1
        backtrace(0, [])
        return paths

            