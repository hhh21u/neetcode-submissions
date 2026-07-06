class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        res = 0
        while q:
            lenq = len(q)
            for _ in range(lenq):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    count -= 1
            if q:
                res += 1

        return res if count == 0 else -1
        