class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        visited = {}
        worDict = set(wordDict)
        def dfs(start, end):
            if start >= n:
                return True
            if end > n: 
                return False
            if (start, end) in visited: return visited[(start, end)]
            visited[(start, end)] = dfs(start, end + 1)
            if s[start:end] in wordDict:
                visited[(start, end)] = visited[(start, end)] or dfs(end, end)
            return visited[(start, end)]

        return dfs(0, 0)
