class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        l = 0
        n = len(s)
        s_count = defaultdict(int)
        minLen = float("inf")
        res = ""
        have, need = 0, len(t_count)
        for r in range(n):
            c = s[r]
            if c in t_count:
                s_count[c] += 1
                if s_count[c] == t_count[c]:
                    have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    res = s[l:r + 1]
                    minLen = r - l + 1

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        have -= 1
                l += 1
            
        return res 
