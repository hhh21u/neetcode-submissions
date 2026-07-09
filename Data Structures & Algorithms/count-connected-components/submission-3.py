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
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(a):
            visited.add(a)
            for b in adj[a]:
                if b in visited:
                    continue
                dfs(b)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count

        

