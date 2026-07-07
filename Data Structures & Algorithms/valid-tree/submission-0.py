class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for u, v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)

        visited = set()
        cycle = set()

        def dfs(node):
            print(f"cur: {node}")
            if node in cycle:
                return False
            cycle.add(node)
            res = True
            for nxt in adjMap[node]:
                # print(f"nxt {nxt}")
                if (node, nxt) in visited or (nxt, node) in visited:
                    continue
                visited.add((node, nxt))
                res = res and dfs(nxt)
            # print(f"{node}: {res}")
            return res
        res = dfs(0)
        return res if len(visited) == len(edges) else False

