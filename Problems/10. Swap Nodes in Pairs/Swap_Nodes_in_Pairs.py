# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
                previous = temp
        while previous.next != None and previous.next.next:
            node1 = previous.next
            node2 = previous.next.next
            previous.next = node2
            node1.next = node2.next
            node2.next = node1
            previous = node1
        return temp.next
        