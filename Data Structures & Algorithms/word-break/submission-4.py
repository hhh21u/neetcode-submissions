class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordset = set(wordDict)
        t = len(wordDict[0])
        for w in wordDict:
            t = max(t, len(w))
        memo = {}
        def dfs(idx):
            if idx in memo: return memo[idx]
            if idx == n:
                return True
            if idx > n: return False
            for end in range(idx, min(n, idx + t)):
                if s[idx: end + 1] in wordDict:
                    if dfs(end + 1):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False
        return dfs(0)

