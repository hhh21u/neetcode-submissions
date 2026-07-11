class UnionSet:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [0] * size
    
    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        # print(self.parents)
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sizes[px] >= self.sizes[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        else:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        unionset = UnionSet(len(edges) + 1)
        cycle_pair = [0, 0]
        for u, v in edges:
            if unionset.union(u, v) == False:
                cycle_pair = [u, v]
        return cycle_pair


        