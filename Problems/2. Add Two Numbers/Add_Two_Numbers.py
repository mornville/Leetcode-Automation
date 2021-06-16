# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        ansNode = ListNode(0)
        p3 = ansNode
        tempVal = ListNode(0)
        carry = 0
                while p1 is not None and p2 is not None:
            tempVal.val = (p1.val + p2.val + carry)%10 
            p3.next = tempVal
            p3 = p3.next
            carry = (p1.val + p2.val + carry)//10
            p1 = p1.next
            p2 = p2.next
            tempVal = ListNode(0)
            ## when len(l1) > len(l2)        
        while p1 is not None:
            tempVal.val = (p1.val + carry) % 10
            p3.next = tempVal
            p3 = p3.next
            carry = (p1.val + carry) // 10           
            p1 = p1.next
            tempVal = ListNode(0)
                            ## when len(l1) < len(l2)
        while p2 is not None:
            print('in p2')
            tempVal.val = (p2.val + carry) % 10
            p3.next = tempVal
            p3 = p3.next
            carry = (p2.val + carry) // 10                      
            p2 = p2.next
            tempVal = ListNode(0)
                    ## check if any carry is left after adding last digits
        if carry:
            tempVal.val = carry
            p3.next = tempVal
            p3 = p3.next
                    return ansNode.next