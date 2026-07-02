class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {} # (x, y) -> count
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        def dfs(x, y):
            if (x, y) in memo: 
                return memo[(x, y)]
            memo[(x, y)] = 1
            for i, j in dirs:
                nx, ny = x + i, y + j
                if nx < 0 or ny < 0 or nx >=m or ny >= n:
                    continue
                sub = 1
                if matrix[x][y] < matrix[nx][ny]:
                    sub += dfs(nx, ny)
                memo[(x,y)] = max(sub, memo[(x,y)])
            # print(f"{x}, {y}, {memo[(x, y)]}")
            return memo[(x, y)]
        

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return max(memo.values())
                    
