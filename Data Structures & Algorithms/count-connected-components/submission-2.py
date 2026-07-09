class UnionSet:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [0] * size
        self.count = size
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.count -= 1
        if self.sizes[px] >= self.sizes[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        else:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        unionset = UnionSet(n)
        for u, v in edges:
            unionset.union(u, v)
        count = set()
        # print(unionset.parents)
        for x in unionset.parents:
            count.add(unionset.find(x))
        return len(count)

