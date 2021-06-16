# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        current = head
        indices = []
        stack = []
        count = 0
        while current:
            indices.append(0)
            value = current.val
            while stack and stack[-1][0] < value:
                x, index = stack.pop()
                indices[index] = value
                        stack.append((value, count))
            count += 1
            current = current.next
                    return indices