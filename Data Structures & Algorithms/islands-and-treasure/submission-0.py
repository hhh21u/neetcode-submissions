class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1

        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(x, y):
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == -1:
                    continue
                if grid[nx][ny] > grid[x][y] + 1:
                    grid[nx][ny] = grid[x][y] + 1
                    dfs(nx, ny)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)

        # return grid
