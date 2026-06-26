class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            maxf = max(maxf, d[s[r]])
            while (r - l + 1) - maxf > k:
                d[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        return res
                        
        