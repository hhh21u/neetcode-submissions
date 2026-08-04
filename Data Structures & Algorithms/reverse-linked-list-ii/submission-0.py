# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        root = ListNode(0, head)
        mainPrev, cur = root, head
        # track position
        i = 1 
        while i < left:
            mainPrev, cur = cur, cur.next
            i += 1
        
        prev = None
        while i <= right:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
            i += 1
        mainPrev.next.next = cur
        mainPrev.next = prev

        return root.next
        