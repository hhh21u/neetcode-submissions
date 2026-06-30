class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        dirs = [(0, 1), (1, 0)]
        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            if x == m - 1 and y == n - 1:
                return 1
            memo[(x,y)] = 0
            for i, j in dirs:
                nx, ny = x + i, y + j
                if nx < 0 or ny < 0 or nx > m or ny > n:
                    continue
                memo[(x,y)] += dfs(nx, ny)
            return memo[(x, y)]
        return dfs(0, 0)
            
            