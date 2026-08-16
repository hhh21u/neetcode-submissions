class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = "-1"

            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != "1":
                    continue
                dfs(nx, ny)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
        