# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        itr = head
        while itr is not None and itr.next is not None:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next 
                        return head