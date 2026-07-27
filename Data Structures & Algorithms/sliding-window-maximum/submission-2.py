class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []# maintain k sized priority queue # (value, index)
        res = []
        for i in range(k - 1):
            heapq.heappush(pq, (-nums[i], i))
        
        for j in range(k - 1, len(nums)):
            left = j - k
            heapq.heappush(pq, (-nums[j], j))
            # print(pq)
            largest, index = heapq.heappop(pq)
            while index <= left:
                largest, index = heapq.heappop(pq)
            
            res.append(-largest)
            heapq.heappush(pq, (largest, index))
        return res