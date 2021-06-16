# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1, p2, temp = head, head, head
        count = 0
        while temp is not None:
            temp = temp.next
            count+=1
        print(count)
        if count <= 1:
            return head
        i = 1
        while i < k:
            p1 = p1.next
            i+=1
        i = 1
        while i <= count-k:
            p2 = p2.next
            i+=1
                 temp = p2.val
        p2.val = p1.val
        p1.val = temp
        print(i - 1)
        return head