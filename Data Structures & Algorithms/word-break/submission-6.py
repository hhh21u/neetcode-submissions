class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordset = set(wordDict)
        t = len(wordDict[0])
        for w in wordDict:
            t = max(t, len(w))
        # memo = {}
        # def dfs(idx):
        #     if idx in memo: return memo[idx]
        #     if idx == n:
        #         return True
        #     if idx > n: return False
        #     for end in range(idx, min(n, idx + t)):
        #         if s[idx: end + 1] in wordDict:
        #             if dfs(end + 1):
        #                 memo[idx] = True
        #                 return True
        #     memo[idx] = False
        #     return False
        # return dfs(0)

        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for w in wordset:
                le = len(w)
                end = i + le
                if end <= n and s[i:end] == w and dp[end] == True:
                    dp[i] = True
                if dp[i]: 
                    break
        return dp[0]


