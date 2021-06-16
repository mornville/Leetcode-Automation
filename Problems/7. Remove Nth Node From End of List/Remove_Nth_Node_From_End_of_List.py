# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        prev = None
        while n>1:
            fast = fast.next
            n-=1
                while fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next
                    if prev == None:
            head = head.next            
        else:
            prev.next = slow.next        
                return head
        