class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        status = [[float("inf") for _ in range(k + 2)] for _ in range(n)]
        # status[city][stop] = bestCost

        pq = []
        adjMap = defaultdict(list) # source: (dst, cost)

        for u, v, c in flights:
            adjMap[u].append((v, c))
        
        heapq.heappush(pq, (0, src, 0))

        while pq:
            cost, cur, stops = heapq.heappop(pq)
            if cur == dst:
                return cost
            if stops > k:
                continue
            for nxt, n_c in adjMap[cur]:
                new_cost = cost + n_c
                n_stop = stops + 1
                if status[nxt][n_stop] > new_cost:
                     status[nxt][n_stop] = new_cost
                     heapq.heappush(pq, (new_cost, nxt, n_stop))
        return -1


        