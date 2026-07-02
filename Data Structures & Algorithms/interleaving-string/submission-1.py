class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        # memo = {}
        # def dfs(idx1, idx2, cur):
        #     if (idx1, idx2, cur) in memo:
        #         return memo[(idx1, idx2, cur)]
        #     if cur == n:
        #         return idx1 == len(s1) and idx2 == len(s2)

        #     if idx1 < len(s1) and s3[cur] == s1[idx1]:
        #         if dfs(idx1 + 1, idx2, cur+1):
        #             memo[(idx1, idx2, cur)] = True
        #             return True
        #     if idx2 < len(s2) and s3[cur] == s2[idx2]:
        #         if dfs(idx1, idx2 + 1, cur + 1):
        #             memo[(idx1, idx2, cur)] = True
        #             return True
        #     memo[(idx1, idx2, cur)] = False
        #     return False

        # return dfs(0, 0, 0)

        n1, n2 = len(s1), len(s2)
        if n1 + n2 != n : return False
        dp = [[False] * (n1 + 1) for _ in range(n2 + 1)]
        dp[n2][n1] = True
        for i in range(n2, -1, -1):
            for j in range(n1, -1, -1):
                if i < n2 and s3[i + j] == s2[i] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n1 and s3[i + j] == s1[j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
        