class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # right or down
        m, n = len(grid), len(grid[0])
        res = [float("inf")]

        q = [] # (timesofar, x, y)
        heapq.heappush(q, (grid[0][0], 0, 0))

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        visited.add((0, 0))

        while q:
            timesofar, x, y = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return timesofar
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                heapq.heappush(q, (max(timesofar, grid[nx][ny]), nx, ny))
        return -1
                    


        

            