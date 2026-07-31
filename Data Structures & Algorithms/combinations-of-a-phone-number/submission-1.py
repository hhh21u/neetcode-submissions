class Solution:
    def __init__(self):
        self.MAP = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        def bt(idx, path):
            if idx == len(digits):
                res.append("".join(path))
                return
            
            for c in self.MAP[digits[idx]]:
                path.append(c)
                bt(idx + 1, path)
                path.pop()
        bt(0, [])
        return res