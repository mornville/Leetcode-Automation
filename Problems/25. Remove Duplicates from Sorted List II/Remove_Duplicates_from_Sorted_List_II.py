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
        temp = ListNode()
        prev = temp
        while itr is not None:
            if itr.next is not None and itr.next.val == itr.val:
                value = itr.val
                while itr is not None and itr.val == value:
                    itr = itr.next
            else:
                prev.next = itr
                prev = prev.next
                itr = itr.next
        prev.next = None
        return temp.next