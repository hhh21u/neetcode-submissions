class Solution:
    def __init__(self):
        self.MAP = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs', 
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        def bt(idx, path):
            if idx == len(digits):
                res.append(path)
                return
            
            for c in self.MAP[digits[idx]]:
                bt(idx + 1, path + c)
        bt(0, '')
        return res