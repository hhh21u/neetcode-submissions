class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        n = len(intervals)
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, n):
            nxtS, nxtE = intervals[i][0], intervals[i][1]
            if end >= nxtS:
                end = max(end, nxtE)
                continue
            else:
                res.append([start, end])
                start, end = nxtS, nxtE
        res.append([start, end])
        return res