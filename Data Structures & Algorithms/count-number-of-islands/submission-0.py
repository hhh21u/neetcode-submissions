class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            for i, j in dirs:
                nx, ny = x + i, y + j
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == -1 or grid[nx][ny] == "0":
                    continue
                grid[nx][ny] = -1
                dfs(nx, ny)
            return
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count