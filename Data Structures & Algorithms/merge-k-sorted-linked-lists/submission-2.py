# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        if self.node.val < other.node.val:
            return True
        return False

class Solution: 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for l in lists:
            if l.val is not None:
                heapq.heappush(pq, NodeWrapper(l))
        res = ListNode(0)
        dummy = res
        while pq:
            cur = heapq.heappop(pq)
            dummy.next = ListNode(cur.node.val)
            dummy = dummy.next
            if cur.node.next is not None:
                heapq.heappush(pq, NodeWrapper(cur.node.next))
        return res.next