class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == 0:
                    perimeter[0] += 1
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                dfs(nx, ny)
        perimeter = [0]
        visited = set()
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    dfs(i, j)
                    return perimeter[0]
                    
