class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        memo = {}
        def dfs(idx1, idx2, cur):
            if (idx1, idx2, cur) in memo:
                return memo[(idx1, idx2, cur)]
            if cur == n:
                return idx1 == len(s1) and idx2 == len(s2)

            if idx1 < len(s1) and s3[cur] == s1[idx1]:
                if dfs(idx1 + 1, idx2, cur+1):
                    memo[(idx1, idx2, cur)] = True
                    return True
            if idx2 < len(s2) and s3[cur] == s2[idx2]:
                if dfs(idx1, idx2 + 1, cur + 1):
                    memo[(idx1, idx2, cur)] = True
                    return True
            memo[(idx1, idx2, cur)] = False
            return False

        return dfs(0, 0, 0)
        