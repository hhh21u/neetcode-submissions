"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        res = dummy = Node(0, None, None)
        node2idx = {}
        arr = []
        new_nodes = []
        i = 0
        while head:
            node2idx[head] = i
            new = Node(head.val, head.next, head.random)
            arr.append(head)
            new_nodes.append(new)
            head = head.next
            i += 1
        i = 0
        for i in range(len(new_nodes)):
            start = new_nodes[i]
            start.random = new_nodes[node2idx[start.random]] if start.random is not None else None
            start.next = new_nodes[node2idx[start.next]] if start.next is not None else None
            start = start.next
        return new_nodes[0] if new_nodes else None



