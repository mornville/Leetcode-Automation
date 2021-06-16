# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
#         arr = []
#         ans = 0
#         while head is not None:
#             arr.append(head.val)
#             head = head.next
                #         i = len(arr) - 1
        #         while i>=0:
#             ans+=(arr[i]) * pow(2, len(arr) -1 - i)
#             i-=1
        #         return ans
        ans = 0
        while head is not None:
            ans = ans<<1
            ans+=head.val
            head = head.next
        return ans