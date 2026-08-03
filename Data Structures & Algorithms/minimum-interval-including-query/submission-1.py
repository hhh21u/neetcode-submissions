class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        res = {}
        i = 0
        pq = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i][0], intervals[i][1]
                heapq.heappush(pq, (r - l + 1, r))
                i += 1
            
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            res[q] = pq[0][0] if pq else -1
        ans = [res[q] for q in queries]
        return ans
