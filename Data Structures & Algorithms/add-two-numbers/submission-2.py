# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        remain = 0
        while l1 or l2:
            val1, val2 = 0, 0
            if l1 and l1.val: val1 = l1.val
            if l2 and l2.val: val2 = l2.val
            # print(f"l1: {val1}, l2: {val2}, remain: {remain}")
            total = val1 + val2 + remain
            if total >= 10:
                res.next = ListNode(total % 10)
                remain = math.floor(total / 10)
            else:
                res.next = ListNode(total)
                remain = 0
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            res = res.next
        
        if remain > 0:
            res.next = ListNode(remain, None)
        else:
            res.next = None
        return dummy.next
