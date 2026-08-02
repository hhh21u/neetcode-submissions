class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst: return 0
        # BFS 
        # revert flights to adjMap
        dist = [[float("inf") for _ in range(k + 5)] for _ in range(n)] # [city][stopused] bestCost sofar
        adjMap = defaultdict(list)
        for fro, to, cost in flights:
            adjMap[fro].append((to, cost))

        # deque [(src, cost)] -> (src, 0)
        # q = deque([(src, 0)])
        # pq [cost, src, stop] -> (0, src, 0)
        q = []
        heapq.heappush(q, (0, src, 0))
    

        # bfs loop iterate all possible next steps
        # break the path if the # of stops is already > k

        while q:
            cost, flight, num = heapq.heappop(q)
            if flight == dst:
                return cost
            if num > k or dist[flight][num] < cost:
                continue
            for nxt, n_cost in adjMap[flight]:
                new_cost = cost + n_cost
                new_stop = num + 1
                if dist[nxt][new_stop] > new_cost:
                    dist[nxt][new_stop] = new_cost
                    heapq.heappush(q, (new_cost, nxt, new_stop))
            
        return -1


