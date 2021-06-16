# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        temp = head     
                while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        head = prev
                    return head
       