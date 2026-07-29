# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or lists[0].val == None:
            return None
    
        def divide(l, r):
            if l > r:
                return None
            if l == r: 
                return lists[l]
            
            mid = (l + r + 1) // 2
            left = divide(l, mid - 1)
            right = divide(mid, r)

            return conquer(left, right)
        
        def conquer(l, r):
            dummy = ListNode(0)
            res = dummy

            while l and r:
                if l.val < r.val:
                    res.next = l
                    l = l.next
                else:
                    res.next = r
                    r = r.next
                res = res.next
            
            if l:
                res.next = l
            if r:
                res.next = r
            return dummy.next

        return divide(0, len(lists) - 1)




