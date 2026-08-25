class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # start with grid n * n dot
        # iterate through row - 
        # for each row position, check if this pos has upper, upperL, upperR Q already there
        res = []
        dirs = [(-1, 0), (-1, -1), (-1, 1)]
        def dfs(row, grid):
            if row == n:
                res.append(grid.copy())
                return
            
            for i in range(n):
                isValid = True
                for dx, dy in dirs:
                    nx, ny = row + dx, i + dy
                    while nx >= 0 and ny >= 0 and nx < n and ny < n: 
                        if grid[nx][ny] == "Q":
                            isValid = False
                            break
                        nx, ny = nx + dx, ny + dy
                    if isValid is False: break
                if isValid:
                    grid[row] = grid[row][:i] + "Q" + grid[row][i + 1:]
                    dfs(row + 1, grid)
                    grid[row] = grid[row][:i] + "." + grid[row][i + 1:]

        grid = ["." * n for _ in range(n)]
        
        dfs(0, grid)
        return res
