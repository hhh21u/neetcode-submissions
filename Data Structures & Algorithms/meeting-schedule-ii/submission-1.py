"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 0 start
        # 5 start
        # 10 end
        # 15 start
        # 20 end
        # 40 end
        status_map = {"start": 0, "end": 1}

        events_pq = []
        for entry in intervals:
            heapq.heappush(events_pq, (entry.start, 1))
            heapq.heappush(events_pq, (entry.end, 0))
        count = 0
        maxRes = 0
        while events_pq:
            start_time, status = heapq.heappop(events_pq)
            # print(f"{start_time}, status: {status}")
            if status == 1:
                count += 1
                maxRes = max(maxRes, count)
            else:
                count -= 1
        return maxRes