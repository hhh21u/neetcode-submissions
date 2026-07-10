class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        pq = []

        for stone in stones:
            heapq.heappush(pq, stone * -1)

        while len(pq) >= 2: 
            x = - heapq.heappop(pq)
            y = - heapq.heappop(pq)
            print(f"{x}, {y}")
            if x < y or y < x:
                heapq.heappush(pq, -(abs(y - x)))
        # print(pq)
        return 0 if len(pq) == 0 else -heapq.heappop(pq)