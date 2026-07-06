"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.dict = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copy = Node(node.val)
        self.dict[node] = copy
        for nei in node.neighbors:
            if nei in self.dict:
                copy.neighbors.append(self.dict[nei])
            else:
                copy.neighbors.append(self.cloneGraph(nei))
        return copy