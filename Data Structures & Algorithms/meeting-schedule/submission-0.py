"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        prevs, preve = -1, -1
        for interval in intervals:
            s, e = interval.start, interval.end
            if s < preve:
                return False
            prevs, preve = s, e
        return True