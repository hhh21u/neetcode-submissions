class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # start with grid n * n dot
        # iterate through row - 
        # for each row position, check if this pos has upper, upperL, upperR Q already there
        res = []
        dirs = [(-1, 0), (-1, -1), (-1, 1)]
        grid = ["." * n for _ in range(n)]
        def dfs(row):
            if row == n:
                res.append(grid.copy())
                return
            
            for i in range(n):
                if isValidPos(row, i):
                    grid[row] = grid[row][:i] + "Q" + grid[row][i + 1:]
                    dfs(row + 1)
                    grid[row] = grid[row][:i] + "." + grid[row][i + 1:]
        
        def isValidPos(x, y):
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                while nx >= 0 and ny >= 0 and nx < n and ny < n: 
                    if grid[nx][ny] == "Q":
                        return False
                    nx, ny = nx + dx, ny + dy
            return True
        dfs(0)
        return res
