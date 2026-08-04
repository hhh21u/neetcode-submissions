"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        # create minHeap (time, end: 0 start: 1)
        events = []
        for interval in intervals:
            start, end = interval.start, interval.end
            heapq.heappush(events, (start, 1))
            heapq.heappush(events, (end, 0))
        count = 0
        res = 0
        while(events):
            time, typ = heapq.heappop(events)
            if typ == 1: #start
                count += 1
            elif typ == 0:
                count -= 1
            res = max(res, count)
        return res

        # [ 0 1, 8 0, 8 1, 10 0]