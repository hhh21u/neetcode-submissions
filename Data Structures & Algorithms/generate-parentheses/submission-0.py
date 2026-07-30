class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(l, r, path): # remain_left, remain_right, path
            if l + r == 0:
                res.append("".join(path))
                return 
            
            if l > 0:
                path.append("(")
                backtrack(l - 1, r + 1, path)
                path.pop()
            if r > 0:
                path.append(")")
                backtrack(l, r - 1, path)
                path.pop()
        
        backtrack(n, 0, [])
        return res