class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedPacific = set()
        visitedAtlantic = set()
        pacific, atlantic = [], []
        m, n = len(heights), len(heights[0])
        if m == 1 and n == 1: return [[0, 0]]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        
        def dfs(x, y, isPacific):
            if isPacific:
                visitedPacific.add((x, y))
            else:
                if (x, y) not in visitedAtlantic:
                    visitedAtlantic.add((x, y))
                    if (x, y) in visitedPacific:
                        res.append((x, y))
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if (isPacific and (nx, ny) in visitedPacific) or (not isPacific and (nx, ny) in visitedAtlantic):
                    continue
                if heights[nx][ny] >= heights[x][y]:
                    # print(f"{isPacific}, {nx}, {ny}")
                    dfs(nx, ny, isPacific)

        for j in range(n):
            dfs(0, j, True)
        for i in range(m):
            dfs(i, 0, True)
        
        for j in range(n):
            dfs(m - 1, j, False)
        for i in range(m):
            dfs(i, n - 1, False)

        return sorted(res)