class Solution:
    def countSubstrings(self, s: str) -> int:
        sum_res = 0
        n = len(s)
        
        def expand(l, r):
            sub = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                sub += 1
            return sub
        
        for i in range(n):
            sum_res += expand(i, i)
            sum_res += expand(i, i + 1)
        return sum_res

        