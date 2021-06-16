# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: 
            return head 
                mid = self.getMid(head)
        next = mid.next
        mid.next = None
                right = self.sortList(next)
        left = self.sortList(head)
                sortedList = self.mergeSorted(left, right)
                return sortedList
        def getMid(self, head):
        if head == None: 
            return head 
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
        def mergeSorted(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
                if left.val <= right.val: 
            result = left 
            result.next = self.mergeSorted(left.next, right) 
        else: 
            result = right 
            result.next = self.mergeSorted(left, right.next) 
        return result 
        