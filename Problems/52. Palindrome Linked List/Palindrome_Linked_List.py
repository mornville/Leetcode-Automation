# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            popped = stack.pop()
            if temp.val == popped:
                temp = temp.next
            else:
                return False
        return True
        