class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and r >= 0 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        bestres = 0
        bestl = 0
        for i in range(n):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)
            len1 = (r1 - l1 + 1)
            len2 = r2 - l2 + 1
            if len1 >= bestres:
                bestres = len1
                bestl = l1
            if len2 >= bestres:
                bestres = len2
                bestl = l2
        return s[bestl: bestl+bestres]
