class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        # memo = {}
        # def dfs(idxs, idxt):
        #     if (idxs, idxt) in memo:
        #         return memo[(idxs, idxt)]
        #     if idxt == nt:
        #         return 1
        #     if idxs >= ns:
        #         return 0
        #     memo[(idxs, idxt)] = dfs(idxs + 1, idxt)
        #     if s[idxs] == t[idxt]:
        #         memo[(idxs, idxt)] += dfs(idxs + 1, idxt + 1)
        #     return memo[(idxs, idxt)]

        # return dfs(0, 0)
            
        dp = [[0] * (nt + 1) for _ in range(ns + 1)]
        for i in range(ns + 1):
            dp[i][nt] = 1
        
        for i in range(ns - 1, -1, -1):
            for j in range(nt - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]



