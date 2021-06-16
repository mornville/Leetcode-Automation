# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode()
        if l1 is None:
            return l2
        if l2 is None:
            return l1
                if(l1.val <= l2.val):
            temp.val = l1.val
            temp.next = self.mergeTwoLists(l1.next, l2)
        else:
            temp.val = l2.val
            temp.next = self.mergeTwoLists(l2.next, l1)
                    return temp