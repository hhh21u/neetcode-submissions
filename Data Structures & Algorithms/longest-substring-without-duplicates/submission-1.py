class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2: return n
        res = 0
        l, r = 0, 0
        visited = set([s[0]])
        while r < n - 1:
            r += 1
            while s[r] in visited:
                visited.discard(s[l])
                l += 1
            visited.add(s[r])
            res = max(res, r - l + 1)
        return res
