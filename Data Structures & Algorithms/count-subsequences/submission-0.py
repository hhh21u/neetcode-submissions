class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        memo = {}
        def dfs(idxs, idxt):
            if (idxs, idxt) in memo:
                return memo[(idxs, idxt)]
            if idxt == nt:
                return 1
            if idxs >= ns:
                return 0
            memo[(idxs, idxt)] = dfs(idxs + 1, idxt)
            if s[idxs] == t[idxt]:
                memo[(idxs, idxt)] += dfs(idxs + 1, idxt + 1)
            return memo[(idxs, idxt)]

        return dfs(0, 0)
            
            