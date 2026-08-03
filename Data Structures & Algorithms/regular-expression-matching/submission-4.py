class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        memo = {}

        def dp(idx_s, idx_p):
            if (idx_s, idx_p) in memo:
                return memo[(idx_s, idx_p)]
            if idx_p == np:
                return idx_s == ns

            match = (idx_s < ns and (p[idx_p] == "." or p[idx_p] == s[idx_s]))
            if idx_p != np - 1 and p[idx_p + 1] == "*":
                result = (dp(idx_s, idx_p + 2) 
                or (match and dp(idx_s + 1, idx_p)))
            else:
                result = match and dp(idx_s + 1, idx_p + 1)
            memo[(idx_s, idx_p)] = result
            return result

        return dp(0, 0)

