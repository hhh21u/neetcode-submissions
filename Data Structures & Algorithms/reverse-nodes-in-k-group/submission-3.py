# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        def getKth(node):
            count = 0
            while node and count < k:
                count += 1
                node = node.next
            return node

        while True:
            kth = getKth(groupPrev)
            if not kth: break
            groupNext = kth.next

            cur, prev = groupPrev.next, kth.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next


        
        

            

            
