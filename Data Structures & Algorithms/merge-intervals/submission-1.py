class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        if n <= 1:
            return intervals
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for nxtStart, nxtEnd in intervals[1:]:
            if end < nxtStart:
                res.append([start, end])
                start, end = nxtStart, nxtEnd
            else:
                end = max(end, nxtEnd)
        res.append([start, end])
        return res