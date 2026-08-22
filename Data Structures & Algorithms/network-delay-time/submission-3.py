class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set([k])

        adj_map = defaultdict(list)
        pq = []
        for time in times:
            u, v, t = time[0], time[1], time[2]
            adj_map[u].append((v, t))
            if u == k:
                heapq.heappush(pq, (t, v))
        res = 0
        while pq:
            print(pq)
            t, v = heapq.heappop(pq)
            if v in visited:
                continue
            res = max(res, t)
            visited.add(v)
            for adj, n_t in adj_map[v]:
                if adj in visited:
                    continue
                heapq.heappush(pq, (n_t + t, adj))
        return res if len(visited) == n else -1