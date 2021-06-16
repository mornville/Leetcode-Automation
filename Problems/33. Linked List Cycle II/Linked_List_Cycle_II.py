# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
                while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next  
            if slow==fast:
                slow=head
                while slow:
                    if slow==fast:
                        return slow
                    slow=slow.next
                    fast=fast.next
        return None