class UnionSet:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1] * size
        self.maxSize = 1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sizes[px] >= self.sizes[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
            self.maxSize = max(self.maxSize, self.sizes[px])
        else:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
            self.maxSize = max(self.maxSize, self.sizes[py])
        return True
    
class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        unionset = UnionSet(m * n)

        q = deque([])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = 1
                    idx = i * n + j
                    for dx, dy in dirs:
                        nx, ny = dx + i, dy + j
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                            continue
                        nidx = nx * n + ny
                        unionset.union(idx, nidx)
        # print(unionset.parents)
        return unionset.maxSize if res != 0 else 0
