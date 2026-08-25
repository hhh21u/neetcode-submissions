class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: 
            return [["Q"]]
        grid = [["."] * n for _ in range(n)]
        res = []
        colset = set()
        dialogset = set() # row - col
        antidset = set() # row + col

        def dp(r):
            if r == n:
                res.append(["".join(r) for r in grid])
                return
            for c in range(n):
                if c in colset or (r - c) in dialogset or (r + c) in antidset:
                    continue
                grid[r][c] = "Q"
                colset.add(c)
                dialogset.add(r-c)
                antidset.add(r + c)
                dp(r + 1)
                grid[r][c] = "."
                colset.remove(c)
                dialogset.remove(r-c)
                antidset.remove(r + c)
        dp(0)
        return res
            
