class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        q = deque([])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    count = 0
                    q.append((i, j))
                    count = 1
                    while q:
                        lenq = len(q)
                        for _ in range(lenq):
                            x, y = q.popleft()
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                                    continue
                                grid[nx][ny] = -1
                                count += 1
                                q.append((nx, ny))
                    res = max(res, count)
        return res
