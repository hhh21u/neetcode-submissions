class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bottom up dp
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_res = 0
        best_l = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > best_res:
                        best_res = j - i + 1
                        best_l = i
        # print(dp)
        return s[best_l: best_l + best_res]
        
