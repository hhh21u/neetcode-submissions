class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: 
            return [["Q"]]
        grid = ["." * n for _ in range(n)]
        res = []
        colset = set()
        dialogset = set() # row - col
        antidset = set() # row + col

        def dp(r):
            if r == n:
                res.append(grid.copy())
                return
            for c in range(n):
                if c in colset or (r - c) in dialogset or (r + c) in antidset:
                    continue
                grid[r] = grid[r][:c] + "Q" + grid[r][c + 1:]
                colset.add(c)
                dialogset.add(r-c)
                antidset.add(r + c)
                dp(r + 1)
                grid[r] = grid[r][:c] + "." + grid[r][c + 1:]
                colset.remove(c)
                dialogset.remove(r-c)
                antidset.remove(r + c)
        dp(0)
        return res
            

    
    def isValidPos(self, x, y, grid):
        dirs = [(-1, -1), (-1, 1), (-1, 0)]
        n = len(grid)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            while nx >= 0 and ny >= 0 and ny < n and nx < n:
                if grid[nx][ny] == "Q":
                    return False
                nx, ny = nx + dx, ny + dy
        return True