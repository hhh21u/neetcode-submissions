class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list) # point to neighbor ((i,j) -> (dist, (i, j)))

        n = len(points)
        for i in range(n):
            x, y = points[i]
            for j in range(n):
                if i == j: continue
                nx, ny = points[j]
                dist = abs(nx - x) + abs(ny - y)
                graph[(x, y)].append((dist, nx, ny))
        start = (points[0][0], points[0][1])

        visited = set()
        visited.add(start)
        count = 0
        pq = []
        for nei in graph[start]:
            heapq.heappush(pq, tuple(nei))
        # print(graph)
        while pq:
            dis, x, y = heapq.heappop(pq)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            # print(f"check order {x}, {y}")
            count += dis
            for nei in graph[(x, y)]:
                if (nei[1], nei[2]) not in visited:
                    heapq.heappush(pq, nei)
        return count
        

