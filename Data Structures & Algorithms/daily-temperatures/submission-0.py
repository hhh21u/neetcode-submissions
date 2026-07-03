class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            cur = temperatures[i]
            while stack and cur > stack[-1][0]:
                pre, idx = stack.pop()
                res[idx] = i - idx
            stack.append((cur, i))
            
        return res