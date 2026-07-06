class UnionSet:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1] * size
    
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
        else:
            self.parents[px] = py
            self.sizes[py] == self.sizes[px]
        return True
        
    
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        union = UnionSet(m * n)
        count = 0
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == "1":
                    idx = i * n + j
                    count += 1
                    for dx, dy in dirs:
                        nx, ny = i + dx, j + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == "0":
                            continue
                        nidx = nx * n + ny
                        if union.union(idx, nidx):
                            count -= 1
        return count
        
                