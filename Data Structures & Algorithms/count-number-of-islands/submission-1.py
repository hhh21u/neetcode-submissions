class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        q = deque([])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    q.append((i, j))
                    while q:
                        lenq = len(q)
                        for _ in range(lenq):
                            x, y = q.popleft()
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny] == "1":
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
        return count
                