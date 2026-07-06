"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {}
        if node is None: return None
        q = deque([node])
        root = Node(node.val)
        old2new[node] = root
        while q:
            lenq = len(q)
            for _ in range(lenq):
                cur = q.popleft()
                copy = old2new[cur]
                for nb in cur.neighbors:
                    if nb not in old2new:
                        nb_cp = Node(nb.val)
                        old2new[nb] = nb_cp
                        q.append(nb)
                    copy.neighbors.append(old2new[nb])
        return root