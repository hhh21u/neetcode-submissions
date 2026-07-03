class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (lastIdx, height)
        res = 0
        for i, h in enumerate(heights):
            cur = heights[i]
            previ = i
            while stack and stack[-1][1] > cur:
                previ, prevh = stack.pop()
                res = max(res, (i - previ) * prevh)
            stack.append((previ, cur))
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        return res
