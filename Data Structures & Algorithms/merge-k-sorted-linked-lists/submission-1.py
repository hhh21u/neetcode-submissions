# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for l in lists:
            while l:
                heapq.heappush(pq, l.val)
                l = l.next
        res = ListNode(0)
        dummy = res
        while pq:
            dummy.next = ListNode(heapq.heappop(pq))
            dummy = dummy.next
        return res.next