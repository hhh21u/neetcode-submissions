class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        # memo = {}

        # def dfs(idx1, idx2):
        #     if (idx1, idx2) in memo:
        #         return memo[(idx1, idx2)]
        #     if idx2 == n2:
        #         return n1 - idx1
        #     if idx1 == n1:
        #         return n2 - idx2
        #     if idx1 >= n1 or idx2 >= n2:
        #         return float("inf")
        #     memo[(idx1, idx2)] = 1 + min(dfs(idx1 + 1, idx2), dfs(idx1 + 1, idx2 + 1), dfs(idx1, idx2 + 1))
        #     if word1[idx1] == word2[idx2]:
        #         memo[(idx1, idx2)] = min(memo[(idx1, idx2)], dfs(idx1 + 1, idx2 + 1))
        #     return memo[(idx1, idx2)]

        # return dfs(0, 0)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == n1:
                    dp[i][j] = n2 - j
                if j == n2:
                    dp[i][j] = n1 - i
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                dp[i][j] = 1 + min(dp[i +1][j], dp[i + 1][j + 1], dp[i][j + 1])
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j + 1])
        return dp[0][0]
        
