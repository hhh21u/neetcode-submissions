# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        start = head.next
        stack = []
        while start:
            stack.append(start)
            start = start.next
        
        tmp = head
        n = len(stack)
        for i in range(len(stack) - 1, math.floor(n/2) - 1, -1):
            prev = tmp.next
            nxt = stack[i]
            tmp.next= nxt
            tmp = tmp.next
            tmp.next = prev
            tmp = tmp.next
        if tmp != None:
            tmp.next = None