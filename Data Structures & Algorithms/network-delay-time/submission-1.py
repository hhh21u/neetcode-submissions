class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []
        visited = set()
        node2neighbors = defaultdict(list)
        for time in times:
            u, v, t = time[0], time[1], time[2]
            node2neighbors[u].append((v, t))

        heapq.heappush(pq, (0, k))
        timeline = [float("inf")] * n
        t = 0
        while pq:
            cur_t, u = heapq.heappop(pq)
            if u in visited:
                continue
            t = cur_t
            visited.add(u)
            for v, t2 in node2neighbors[u]:
                if v not in visited:
                    heapq.heappush(pq, (cur_t + t2, v))
        
        return t if len(visited) == n else -1

