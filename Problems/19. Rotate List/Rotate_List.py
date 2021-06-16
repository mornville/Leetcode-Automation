# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        lis = []
        cur = head
        while cur != None:
            lis.append(cur.val)
            cur = cur.next
        n = len(lis)
        k = k%n
        self.reverse(lis,n-k,n-1)
        self.reverse(lis,0,n-k-1)
        self.reverse(lis,0,n-1)
        temphead = None
        prev = None
        cur = None
        j = 0
        while j < len(lis):
            if temphead == None:
                temphead = ListNode(lis[j])
                prev = temphead
                j = j + 1
            else:
                cur = ListNode(lis[j])
                prev.next = cur
                prev = cur
                cur = cur.next
                j = j + 1
        return temphead
                    def reverse(self,lis,start,end):
        while start < end:
            temp = lis[start]
            lis[start] = lis[end]
            lis[end] = temp
            start = start + 1
            end = end - 1