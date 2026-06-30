class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        n = len(s)
        visited = {}
        def dp(idx):
            if idx >= n:
                return 1
            if idx in visited: return visited[idx]
            visited[idx] = 0
            if s[idx] != "0":
                visited[idx] = dp(idx + 1)

                if idx + 1 < n and int(s[idx:idx + 2]) <= 26:
                    visited[idx] += dp(idx + 2)
            return visited[idx]
        return dp(0)
                
            