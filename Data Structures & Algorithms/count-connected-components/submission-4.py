class UnionSet:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [0] * size
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 0
        if self.sizes[px] >= self.sizes[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        else:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
        return 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionset = UnionSet(n)
        res = n
        for u, v in edges:
            res -= unionset.union(u, v)
        return res
            

        

