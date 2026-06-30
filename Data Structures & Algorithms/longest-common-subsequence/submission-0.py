class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        memo = {}
        def dfs(idx1, idx2):
            if (idx1, idx2) in memo: return memo[(idx1, idx2)]
            if idx1 >= n1 or idx2 >= n2:
                return 0
            memo[(idx1, idx2)] = max(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))
            if text1[idx1] == text2[idx2]:
                memo[(idx1, idx2)] = max(memo[(idx1, idx2)], 1 + dfs(idx1 + 1, idx2 + 1))
            return memo[(idx1, idx2)]

        return dfs(0, 0)
