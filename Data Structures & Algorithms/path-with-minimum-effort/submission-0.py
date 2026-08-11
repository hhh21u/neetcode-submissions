class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        if m == n == 1:
            return 0
        # dijkstra
        def calc_effort(h1, h2):
            return abs(h1 - h2)
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pq = [(0,0,0)] # (distance, x, y)
        dist = [[float("inf") for _ in range(n)] for _ in range(m)]
        routes = 1
        dist[0][0] = 0

        while pq:
            dis, x, y = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return dis
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                effort = calc_effort(heights[x][y], heights[nx][ny])
                n_dis = max(dis, effort)
                if n_dis < dist[nx][ny]:
                    heapq.heappush(pq, (n_dis, nx, ny))
                    dist[nx][ny] = n_dis
        return dist[-1][-1]


