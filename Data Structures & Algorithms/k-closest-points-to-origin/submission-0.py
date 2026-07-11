class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dis = math.sqrt((x ** 2 + y ** 2))
            heapq.heappush(pq, (dis, x, y))
        
        res = []
        for _ in range(k):
            dis, x, y = heapq.heappop(pq)
            res.append((x, y))
        return res