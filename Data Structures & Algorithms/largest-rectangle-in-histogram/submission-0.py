class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (lastIdx, height)
        res = 0
        n = len(heights)
        for i in range(n):
            cur = heights[i]
            previ = i
            while stack and stack[-1][1] > cur:
                previ, prevh = stack.pop()
                res = max(res, (i - previ) * prevh)
            stack.append((previ, cur))
        
        while stack:
            i, h = stack.pop()
            res = max(res, (n - i) * h)
        return res
