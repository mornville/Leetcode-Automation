# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """ Using iteration"""
        """Floyd’s Cycle-Finding Algorithm"""
            slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
        