# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
                if p1 is None or p2 is None:
            return None
                while p1!=p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
                        if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return p1