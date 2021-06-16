# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            # move ahead in the original list
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next