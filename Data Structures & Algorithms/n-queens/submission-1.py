class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: 
            return [["Q"]]
        grid = ["." * n for _ in range(n)]
        res = []

        def dp(r):
            if r == n:
                res.append(grid.copy())
                return
            for c in range(n):
                if self.isValidPos(r, c, grid):
                    grid[r] = grid[r][:c] + "Q" + grid[r][c + 1:]
                    dp(r + 1)
                    grid[r] = grid[r][:c] + "." + grid[r][c + 1:]
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