class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjmap = defaultdict(list)
        for u, v, t in times:
            adjmap[u].append((v, t))
        
        pq = [(0, k)]
        store = {k: 0}
        res = 0
        while pq:
            t, u = heapq.heappop(pq)
            for v, vt in adjmap[u]:
                if v not in store or (v in store and vt + t < store[v]):
                        pq.append((vt + t, v))
                        store[v] = vt + t
        print(store)
        return max(store.values()) if len(store) == n else -1