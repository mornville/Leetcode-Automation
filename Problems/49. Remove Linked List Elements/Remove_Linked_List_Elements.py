# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
                curr = head
        prev = None
                while curr:
            if curr.val == val: 
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
                return head