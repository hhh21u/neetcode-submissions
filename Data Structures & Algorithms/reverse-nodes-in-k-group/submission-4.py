# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p = head
        size = 0
        while p:
            size += 1
            p = p.next

        lastEnd = dummy
        p = head
        for _ in range(size // k):
            prev = None
            for _ in range(k):
                p.next, p, prev = prev, p.next, p
            lastEnd.next, lastEnd = prev, lastEnd.next
            lastEnd.next = p
        if p:
            lastEnd.next = p
        return dummy.next


        
        

            

            
