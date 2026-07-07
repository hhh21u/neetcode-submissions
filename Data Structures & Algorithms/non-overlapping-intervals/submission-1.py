class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        memo = {}

        def dfs(preve, curi):
            if (preve, curi) in memo:
                return memo[(preve, curi)]
            if curi >= n:
                return 0
            curS, curE = intervals[curi][0], intervals[curi][1]
            res = float("inf")
            if preve <= curS:
                res = min(res, dfs(curE, curi + 1))
            else:
                res = min(res, 1 + dfs(preve, curi + 1), 1 + dfs(curE, curi + 1))
            memo[(preve, curi)] = res
            return memo[(preve, curi)]
        
        return dfs(-float("inf"), 0)
                
