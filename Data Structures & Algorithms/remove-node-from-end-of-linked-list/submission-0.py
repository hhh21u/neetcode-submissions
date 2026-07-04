# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        depth = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            depth += 1
        
        idx = depth - n
        if idx == 0:
            return head.next
        start = head
        count = 1
        while start:
            if count == idx:
                start.next = start.next.next
            count += 1
            start = start.next
        return head
